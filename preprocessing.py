import pandas as pd
from sklearn.preprocessing import LabelEncoder

# ==========================
# LOAD DATASET
# ==========================

df = pd.read_csv("dataset/Sleep_health_and_lifestyle_dataset.csv")

print("Jumlah Data Awal :", len(df))

# ==========================
# HAPUS KOLOM YANG TIDAK DIPAKAI
# ==========================

df.drop(columns=["Person ID", "Occupation", "Blood Pressure"], inplace=True)

# ==========================
# TARGET
# NaN dianggap tidak memiliki gangguan tidur
# ==========================

df["Sleep Disorder"] = df["Sleep Disorder"].fillna("Healthy")

# ==========================
# CEK HASIL LABEL
# ==========================

print("\nDistribusi Target")
print(df["Sleep Disorder"].value_counts())

# ==========================
# ENCODING
# ==========================

encoder_gender = LabelEncoder()
encoder_bmi = LabelEncoder()
encoder_target = LabelEncoder()

df["Gender"] = encoder_gender.fit_transform(df["Gender"])
df["BMI Category"] = encoder_bmi.fit_transform(df["BMI Category"])
df["Sleep Disorder"] = encoder_target.fit_transform(df["Sleep Disorder"])

print("\nMapping Target")
for i, label in enumerate(encoder_target.classes_):
    print(i, "=", label)

# ==========================
# SIMPAN DATASET BERSIH
# ==========================

df.to_csv("dataset/clean_dataset.csv", index=False)

print("\nDataset berhasil disimpan.")
print(df.head())