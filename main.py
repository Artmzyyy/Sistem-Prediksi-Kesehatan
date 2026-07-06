import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split  
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import(
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)
encoder = LabelEncoder()
scaler = StandardScaler()
model = LogisticRegression(
    class_weight='balanced',
    max_iter=1000,
    random_state=42
)

df = pd.read_csv('dataset/health_lifestyle_dataset.csv')
df["gender"] = encoder.fit_transform(df["gender"])
df = df.drop("id", axis=1)

x = df.drop("disease_risk", axis=1)
y = df["disease_risk"]

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, 
    random_state=42,
    stratify=y
    )

x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

model = model.fit(x_train, y_train)
y_pred = model.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)



print("Output DF INFO dan HEAD")
print(df.head())
print(df.info())
print("================================")

print("Total Gender")
print(df["gender"].value_counts())
print("===============================")

print(df.describe())
print("\nKorelasi dengan disease_risk")
corr = df.corr(numeric_only=True)
print(corr["disease_risk"].sort_values(ascending=False))
print("===============================")


print(df.isnull().sum())
print(df['disease_risk'].value_counts())
sns.countplot(x='disease_risk', data=df)
plt.title("Distribusi Disease Risk")
plt.show()

print("Output DF COLUMNS")
print(df.columns)
for col in df.columns:
    print(col)
    print(df[col].value_counts().head())
    print("===============================")

print("===============================")
print("Hasil: ")
print("Akurasi: ", accuracy)
print("Confusion Matrix: ", cm)
print("Classification Report: ", classification_report(y_test, y_pred))
print("Precision: ", precision_score(y_test, y_pred))
print("Recall: ", recall_score(y_test, y_pred))
print("F1-Score: ", f1_score(y_test, y_pred))
print("================================")
