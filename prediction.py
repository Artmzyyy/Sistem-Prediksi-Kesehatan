import joblib
import pandas as pd

# Load model dan scaler
model = joblib.load("model/model_gui.pkl")
scaler = joblib.load("model/scaler_gui.pkl")

# Mapping hasil prediksi
hasil_prediksi = {
    0: {
        "status": "Baik",
        "warna": "green",
        "analisis": "Pola tidur dan gaya hidup Anda menunjukkan kondisi yang baik.",
        "saran": "Pertahankan pola hidup sehat dan aktivitas fisik secara rutin."
    },
    1: {
        "status": "Perlu Perhatian",
        "warna": "orange",
        "analisis": "Terdapat indikasi pola yang menyerupai insomnia.",
        "saran": "Perbaiki jadwal tidur dan kurangi begadang."
    },
    2: {
        "status": "Berisiko",
        "warna": "red",
        "analisis": "Terdapat indikasi pola yang menyerupai sleep apnea.",
        "saran": "Disarankan berkonsultasi dengan tenaga kesehatan untuk pemeriksaan lebih lanjut."
    }
}


def prediksi(gender, age, sleep_duration, bmi_category,
             physical_activity, daily_steps):

    data = pd.DataFrame([[
        gender,
        age,
        sleep_duration,
        bmi_category,
        physical_activity,
        daily_steps
    ]], columns=[
        "Gender",
        "Age",
        "Sleep Duration",
        "BMI Category",
        "Physical Activity Level",
        "Daily Steps"
    ])

    data = scaler.transform(data)

    hasil = model.predict(data)[0]

    return hasil_prediksi[hasil]