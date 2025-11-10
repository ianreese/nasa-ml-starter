#!/usr/bin/env python
"""
Train a baseline classifier to predict is_hazardous from numeric features.
Saves model + a text metrics report.
"""
import argparse, os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
import joblib

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--in", dest="inp", required=True, help="Input CSV features")
    parser.add_argument("--model", required=True, help="Path to save model (joblib)")
    args = parser.parse_args()

    df = pd.read_csv(args.inp)
    df = df.dropna()
    X = df[["absolute_magnitude_h","diameter_km_min","diameter_km_max","rel_velocity_km_s","miss_distance_km"]]
    y = df["is_hazardous"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)

    clf = Pipeline([
        ("scaler", StandardScaler()),
        ("logreg", LogisticRegression(max_iter=200))
    ])

    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)
    report = classification_report(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)

    os.makedirs(os.path.dirname(args.model), exist_ok=True)
    joblib.dump(clf, args.model)

    metrics_path = os.path.join(os.path.dirname(args.model), "metrics.txt")
    with open(metrics_path, "w") as f:
        f.write("Classification Report:\n")
        f.write(report + "\n")
        f.write("Confusion Matrix:\n")
        f.write(str(cm) + "\n")

    print(f"Saved model → {args.model}")
    print(f"Saved metrics → {metrics_path}")

if __name__ == "__main__":
    main()
