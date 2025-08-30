# StressSense — Early Stress Risk Screener (End-to-End ML)

A compact, **utility-focused** end-to-end ML project that predicts **stress level** (Low/Moderate/High) from lifestyle and study/work patterns. Built to be **completed in ~2 hours** while satisfying common cohort requirements: **EDA, 2+ ML classifiers, model comparison, explainability, and a tiny demo app**.

---

## ✨ What’s inside
- `notebooks/StressSense_End_to_End.ipynb` — The main notebook (EDA → preprocessing → 2+ models → evaluation → explainability → demo).
- `data/sample_stress_data.csv` — A tiny synthetic CSV to test the pipeline. Replace with your real dataset.
- `models/` — Saved model artifacts will appear here after you run the notebook.
- `artifacts/feature_types.json` — Auto-generated metadata for the demo UI (numeric/categorical columns, ranges, options).
- `app/gradio_app.py` — Launch a small UI to test predictions locally.
- `requirements.txt` — Python dependencies.
- `.gitignore` — Ignore bulky artifacts/venv.
  
---

## 🧪 Dataset Options
Use **any** clean stress dataset (CSV). Two common choices:
1. *Student/Professional Stress Level* datasets on Kaggle (choose one with columns like sleep duration, screen time, study/work hours, caffeine, activity, etc.).
2. UCI-styled lifestyle mental health datasets with clearly labeled `stress_level` as target.

> **Tip:** Ensure your target column is something like `stress_level` with 3 classes *(Low/Moderate/High)*. If your dataset is binary, the notebook still works (Auto-detects classes).

Place your CSV at `data/your_data.csv` and update the path in the notebook.

---

## 🚀 Quickstart (Colab or Local)

### Option A) Google Colab (recommended)
1. Upload this repo to GitHub.
2. Open `notebooks/StressSense_End_to_End.ipynb` in Colab (use the GitHub → Open in Colab button or copy the raw URL).
3. In the notebook:
   - If using your own CSV, upload to Colab or mount Drive and update the `DATA_PATH`.
   - Run cells top-to-bottom.
4. Export **PDF**: *File → Print → Save as PDF* (Colab’s best method).

### Option B) Local (VS Code/Jupyter)
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter lab  # or: jupyter notebook
```
Open the notebook and run it.

---

## 🧩 Launch the Demo App (after training)
Once the notebook saves artifacts, run:
```bash
python app/gradio_app.py
```
A small form will open in the browser where you can input sleep/work hours etc. and get a predicted **stress level + probability**.

---

## 📝 Submission Checklist
- [ ] Clean, runnable notebook with clear sections & outputs.
- [ ] At least **two classifiers** trained & compared (Logistic Regression + RandomForest; optional GradientBoosting).
- [ ] Evaluation with Accuracy, Precision, Recall, F1 (macro for multiclass).
- [ ] Confusion matrix and (optionally) ROC curves.
- [ ] Explainability: feature importance (global) and SHAP (optional).
- [ ] Saved artifacts (pipeline + model).
- [ ] A tiny demo (Gradio) that loads the saved artifacts.
- [ ] PDF exported from the notebook.
- [ ] GitHub repo with README and clean structure.

---

## ⚖️ Ethics & Limitations
- This tool is **not a medical diagnosis**. It’s an educational demonstration to screen **risk** based on reported lifestyle factors.
- Bias can arise from sampling (e.g., only students). Always validate on diverse populations.
- Keep inputs minimal and privacy-preserving.

---

## 📄 License
MIT
