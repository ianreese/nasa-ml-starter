import os
import joblib
import pandas as pd
import matplotlib
matplotlib.use("Agg")  # ensure we save a PNG instead of opening a window
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay

# --- 1) Create folders if missing ---
os.makedirs("data", exist_ok=True)
os.makedirs("artifacts", exist_ok=True)

# --- 2) Load Iris and save a CSV (practice pandas I/O) ---
iris = load_iris(as_frame=True)
df = iris.frame.copy()   # includes 'target'
df.to_csv("data/iris.csv", index=False)

# --- 3) Read CSV back with pandas ---
data = pd.read_csv("data/iris.csv")
X = data.drop(columns=["target"])
y = data["target"]

# --- 4) Train/test split ---
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

# --- 5) Pipeline: scale -> logistic regression ---
clf = Pipeline(steps=[
    ("scaler", StandardScaler()),
    ("logreg", LogisticRegression(max_iter=200))
])

# --- 6) Fit & evaluate ---
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

print("\n=== Classification report ===")
print(classification_report(y_test, y_pred))

cm = confusion_matrix(y_test, y_pred, labels=sorted(y.unique()))
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=sorted(y.unique()))
disp.plot(values_format="d")
plt.title("Iris — LogisticRegression Confusion Matrix")
plt.tight_layout()
plt.savefig("artifacts/iris_confusion_matrix.png")
print("Saved plot → artifacts/iris_confusion_matrix.png")

# --- 7) Save model ---
joblib.dump(clf, "artifacts/iris_logreg.joblib")
print("Saved model → artifacts/iris_logreg.joblib")
