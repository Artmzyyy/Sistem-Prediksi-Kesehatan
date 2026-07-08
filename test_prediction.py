from prediction import prediksi

hasil = prediksi(
    gender=1,
    age=25,
    sleep_duration=7,
    bmi_category=0,
    physical_activity=60,
    daily_steps=8000
)

print(hasil)