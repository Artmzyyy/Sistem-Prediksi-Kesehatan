import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('dataset/Sleep_health_and_lifestyle_dataset.csv')
print("="*60)
print("HEAD")
print("="*60)
print(df.head())

print("="*60)
print("INFO DATASET")
print("="*60)
print(df.info())

print("="*60)
print("STATISTIK")
print("="*60)
print(df.describe())

print("="*60)
print("MISSING VALUE")
print("="*60)
print(df.isnull().sum())

print("="*60)
print("DUPLIKAT")
print("="*60)
print(df.duplicated().sum())

print("="*60)
print("NAMA KOLOM")
print("="*60)
print(df.columns)

print("="*60)

print(df["Sleep Disorder"].value_counts())

sns.countplot(data=df, x="Sleep Disorder")
plt.title("Distribusi Target")
plt.show()

corr = df.corr(numeric_only=True)
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.show()

for col in df.columns:

    print("\n")
    print("="*50)
    print(col)
    print("="*50)

    print(df[col].value_counts().head())

df.hist(figsize=(15,10))
plt.tight_layout()
plt.show()

plt.figure(figsize=(12,8))
sns.boxplot(data=df)
plt.xticks(rotation=90)
plt.show()

sns.pairplot(df)
plt.show()

df["Sleep Disorder"] = df["Sleep Disorder"].fillna("Healthy")
print(df["Sleep Disorder"].unique())
print(df["Sleep Disorder"].value_counts())

