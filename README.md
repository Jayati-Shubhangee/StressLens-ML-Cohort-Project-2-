# 🧠 StressSense — Early Stress Risk Screener

**StressSense** is a compact, end-to-end machine learning project designed to **predict stress levels** (Low / Moderate / High) based on lifestyle, study, and work patterns. It’s practical, privacy-first, and comes with a tiny interactive UI for real-time predictions.  

---

## ✨ Features

- 📊 **End-to-End ML Pipeline**: From data loading → EDA → preprocessing → model training → evaluation → explainability.  
- 🤖 **Multiple Models**: Logistic Regression (baseline), Random Forest (robust), and optional Gradient Boosting.  
- 🔍 **Explainability**: Feature importance and optional SHAP plots to understand what influences stress predictions.  
- 🖥 **Interactive Demo**: Gradio app to test predictions in real-time using sliders and dropdowns.  
- 💾 **Saved Artifacts**: Models and feature metadata saved for reproducibility.  

---

## 📂 Project Structure

StressSense/
│
├── notebooks/
│ └── StressSense_End_to_End.ipynb # Main notebook: EDA → preprocessing → models → evaluation
├── data/
│ └── sample_stress_data.csv # Tiny sample dataset (replace with your real CSV)
├── models/ # Saved model pipelines (auto-generated)
├── artifacts/
│ └── feature_types.json # Metadata for app UI (numeric/categorical info)
├── app/
│ └── gradio_app.py # Launch the interactive demo locally
├── requirements.txt # Python dependencies
├── README.md # This file
└── .gitignore # Ignore virtual environments, models, artifacts

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
💻 Tech Stack

Python 3.10+

pandas, numpy, scikit-learn

joblib (model saving)

Gradio (demo UI)

Jupyter Notebook
---
📌 Future Enhancements

Deploy on Streamlit / Heroku / AWS for public access

Add multi-language support for the app

Incorporate SHAP explanations in the UI

Expand dataset for better model accuracy
