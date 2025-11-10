# NASA ML Starter — Scikit-Learn Demo

A beginner-friendly machine-learning project built to explore **scikit-learn pipelines** and NASA’s public **NeoWs** (Near-Earth Object) API.

It starts with the classic **Iris flower classifier** for fundamentals, then extends to a **hazardous-asteroid detector** using NASA data.

---

## Highlights
-  Logistic-Regression & Scikit-Learn Pipelines  
-  Real NASA NeoWs + APOD API integration  
-  Confusion-Matrix & Model-Evaluation metrics  
-  Virtualenv + requirements.txt environment  
-  Model persistence with `joblib`  

---

## Results
![Confusion Matrix](artifacts/iris_confusion_matrix.png)

*The Iris classifier reached ~92 % accuracy using a simple logistic-regression pipeline.*

---

## Quickstart
```bash
git clone https://github.com/YOUR_USERNAME/nasa-ml-starter.git
cd nasa-ml-starter
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/day2_basics.py

![Confusion Matrix](artifacts/iris_confusion_matrix.png)
