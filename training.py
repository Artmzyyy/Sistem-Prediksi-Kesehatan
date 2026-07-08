import numpy as np
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# ==================================================
# LOAD DATASET
# ==================================================

df = pd.read_csv("dataset/clean_dataset.csv")

print("=" * 50)
print("DATASET")
print("=" * 50)
print(df.head())

# ==================================================
# FEATURE & TARGET
# ==================================================

X = df.drop("Sleep Disorder", axis=1)
y = df["Sleep Disorder"]

feature_names = X.columns

# ==================================================
# TRAIN TEST SPLIT
# ==================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# ==================================================
# STANDARD SCALER
# ==================================================

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# ==================================================
# LOGISTIC REGRESSION
# ==================================================

model = LogisticRegression(
    random_state=42,
    max_iter=3000
)

model.fit(X_train, y_train)

# ==================================================
# PREDIKSI
# ==================================================

y_pred = model.predict(X_test)

# ==================================================
# EVALUASI
# ==================================================

print("\n" + "=" * 50)
print("HASIL EVALUASI")
print("=" * 50)

print(f"Accuracy : {accuracy_score(y_test, y_pred):.4f}")

print("\nClassification Report")
print(classification_report(y_test, y_pred))

print("Confusion Matrix")
print(confusion_matrix(y_test, y_pred))

# ==================================================
# CROSS VALIDATION
# ==================================================

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression(
        random_state=42,
        max_iter=3000
    ))
])

scores = cross_val_score(
    pipeline,
    X,
    y,
    cv=5,
    scoring="accuracy"
)

print("\n" + "=" * 50)
print("CROSS VALIDATION")
print("=" * 50)

print("Accuracy tiap fold :")
print(scores)

print(f"\nRata-rata Accuracy : {scores.mean():.4f}")
print(f"Standar Deviasi    : {scores.std():.4f}")

# ==================================================
# FEATURE IMPORTANCE
# ==================================================

coef = np.abs(model.coef_).mean(axis=0)

importance = pd.DataFrame({
    "Feature": feature_names,
    "Importance": coef
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print("\n" + "=" * 50)
print("FEATURE IMPORTANCE")
print("=" * 50)

print(importance)

# ==================================================
# SIMPAN MODEL
# ==================================================

joblib.dump(model, "model/model.pkl")
joblib.dump(scaler, "model/scaler.pkl")

print("\nModel berhasil disimpan.")