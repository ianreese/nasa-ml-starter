# NASA NeoWs Hazard Classifier + APOD Demo (scikit-learn)

A tiny, week-long starter project to learn **scikit-learn** while playing with the **NASA APIs**.

## What you’ll build
1) A script that fetches **near‑earth objects (NeoWs)** for a short date range and saves a tidy CSV.  
2) A baseline **classification model** (Logistic Regression) predicting the `is_potentially_hazardous_asteroid` flag from physical/orbital features.  
3) A quick **APOD** (Astronomy Picture of the Day) fetcher to show you made a real API call.

> This runs on your Mac with Python 3.10+ (works great in a virtualenv).

---

## Quickstart (Mac)

```bash
# 1) Create & activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate   # fish: source .venv/bin/activate.fish

# 2) Upgrade pip and install deps
python -m pip install --upgrade pip
pip install -r requirements.txt

# 3) Add your NASA API key
cp .env.example .env
# edit .env to set NASA_API_KEY=YOUR_KEY

# 4) Fetch data for the last 3–7 days (<= 7 days allowed by the API)
python src/fetch_nasa.py --start 2025-11-01 --end 2025-11-07 --out data/neows_raw.json
python src/prepare_data.py --in data/neows_raw.json --out data/neows_features.csv

# 5) Train a baseline model
python src/train_model.py --in data/neows_features.csv --model artifacts/model.joblib

# 6) (Optional) Grab the Astronomy Picture of the Day
python src/fetch_apod.py --date 2025-11-07 --out data/apod_2025-11-07.jpg
```

If you don’t have a NASA API key yet, register (free) and paste it into `.env`:
- https://api.nasa.gov/

---

## Project layout

```
nasa-ml-starter/
├─ README.md
├─ requirements.txt
├─ .env.example
├─ .gitignore
├─ data/                # created by you; holds raw & processed files
├─ artifacts/           # trained models, metrics
└─ src/
   ├─ fetch_nasa.py     # calls NeoWs & saves raw JSON
   ├─ prepare_data.py   # converts JSON → tabular CSV
   ├─ train_model.py    # trains a simple scikit-learn classifier
   └─ fetch_apod.py     # downloads APOD image
```

---

## What to learn this week

**Day 1–2 (Scikit‑learn basics)**  
- Understand `train_test_split`, `Pipeline`, `ColumnTransformer`, `StandardScaler`.
- Fit Logistic Regression, plot a simple confusion matrix.

**Day 3 (NASA data)**  
- Call NeoWs with your key; keep ranges ≤ 7 days. Save JSON.

**Day 4 (Feature building)**  
- Extract features: absolute magnitude, min/max estimated diameter, relative velocity (km/s), miss distance (km), approach date.

**Day 5 (Model + eval)**  
- Train baseline model, inspect accuracy, precision/recall/F1. Try RandomForest.

**Weekend stretch**  
- Add cross‑validation and a ROC curve. Try more features (e.g., diameter ratio).

---

## Notes
- The NeoWs feed has `is_potentially_hazardous_asteroid` (boolean) which we’ll predict from numeric features.
- Date windows over 7 days will 400‑error—keep it short.
- This is for learning; don’t treat the model as scientific truth.
