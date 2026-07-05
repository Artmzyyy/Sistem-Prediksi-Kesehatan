import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split  
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import(
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

df = pd.read_csv('dataset/health_lifestyle_dataset.csv')
print("Output DF INFO dan HEAD")
print(df.head())
print(df.info())
print("================================")

print(df.describe())
print(df.isnull().sum())
print(df['disease_risk'].value_counts())
sns.countplot(x='disease_risk', data=df)
plt.title("Distribusi Disease Risk")
plt.show()

print("Output DF COLUMNS")
print(df.columns)


