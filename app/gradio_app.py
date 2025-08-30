import json, joblib, pandas as pd
import gradio as gr
import os

THIS_DIR = os.path.dirname(__file__)
MODEL_PATH = os.path.join(THIS_DIR, '..', 'models', 'stresssense_best_pipeline.pkl')
META_PATH = os.path.join(THIS_DIR, '..', 'artifacts', 'feature_types.json')

if not os.path.exists(MODEL_PATH):
    raise SystemExit("Model not found. Run the notebook to train & save artifacts first.")

model = joblib.load(MODEL_PATH)

with open(META_PATH, 'r') as f:
    meta = json.load(f)

num_cols = meta.get('numeric_cols', [])
cat_cols = list(meta.get('categorical_cols', {}).keys())
ranges = meta.get('ranges', {})

def predict_fn(*values):
    # values order: numeric first (in the same order), then categorical
    inputs = {}
    idx = 0
    for c in num_cols:
        inputs[c] = values[idx]
        idx += 1
    for c in cat_cols:
        inputs[c] = values[idx]
        idx += 1
    X = pd.DataFrame([inputs])
    pred = model.predict(X)[0]
    prob = None
    if hasattr(model.named_steps['clf'], 'predict_proba'):
        probs = model.predict_proba(X)[0]
        classes = model.classes_
        prob = dict(zip(classes, [float(x) for x in probs]))
    msg = f"Prediction: {pred}\n\nProbabilities: {prob}"
    tips = "- Improve sleep routine\n- Balance study/work and screen time\n- Regular physical activity\n- Reduce caffeine later in the day"
    return msg + "\n\nTips:\n" + tips

components = []
labels = []

# Numeric sliders
for c in num_cols:
    lo, hi = ranges.get(c, [0.0, 10.0])
    step = (hi - lo) / 50 if hi > lo else 0.1
    components.append(gr.Slider(minimum=lo, maximum=hi, step=step if step>0 else 0.1, value=(lo+hi)/2 if hi>lo else lo, label=c))
    labels.append(c)

# Categorical dropdowns
for c in cat_cols:
    opts = meta['categorical_cols'].get(c, [])
    default = opts[0] if opts else None
    components.append(gr.Dropdown(choices=opts, value=default, label=c))
    labels.append(c)

demo = gr.Interface(
    fn=predict_fn,
    inputs=components,
    outputs="text",
    title="StressSense — Early Stress Risk Screener",
    description="Enter your lifestyle inputs to estimate stress level (for education only)."
)

if __name__ == "__main__":
    demo.launch()
