import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)

# ===========================================
# LOAD DATASET
# ===========================================

df = pd.read_csv("dataset/clean_dataset.csv")

# ===========================================
# PILIH FITUR YANG AKAN DIPAKAI GUI
# ===========================================

X = df[
    [
        "Gender",
        "Age",
        "Sleep Duration",
        "BMI Category",
        "Physical Activity Level",
        "Daily Steps",
    ]
]

y = df["Sleep Disorder"]

print("=" * 50)
print("FITUR YANG DIGUNAKAN")
print("=" * 50)
print(X.columns)

# ===========================================
# SPLIT DATA
# ===========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y,
)

# ===========================================
# SCALER
# ===========================================

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# ===========================================
# MODEL
# ===========================================

model = LogisticRegression(
    random_state=42,
    max_iter=3000,
)

model.fit(X_train, y_train)

# ===========================================
# PREDIKSI
# ===========================================

y_pred = model.predict(X_test)

print("\n" + "=" * 50)
print("HASIL MODEL GUI")
print("=" * 50)

print(f"Accuracy : {accuracy_score(y_test, y_pred):.4f}")

print("\nClassification Report")
print(classification_report(y_test, y_pred))

print("Confusion Matrix")
print(confusion_matrix(y_test, y_pred))

# ===========================================
# CROSS VALIDATION
# ===========================================

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression(max_iter=3000))
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

print(scores)
print(f"Mean Accuracy : {scores.mean():.4f}")
print(f"Std Accuracy  : {scores.std():.4f}")

# ===========================================
# SIMPAN MODEL
# ===========================================

joblib.dump(model, "model/model_gui.pkl")
joblib.dump(scaler, "model/scaler_gui.pkl")

print("\nModel GUI berhasil disimpan.")