import customtkinter as ctk
from prediction import prediksi
from tkinter import messagebox

def hitung_bmi(bb, tb):
    tinggi = tb / 100
    bmi = bb / (tinggi * tinggi)
    return round(bmi, 2)

def kategori_bmi(bmi):
    if bmi < 18.5:
        return 1  # Underweight
    elif bmi < 25:
        return 0  # Normal
    elif 25 <= bmi < 30:
        return 3  # Overweight
    else:
        return 2  # Obese


def proses_prediksi():

    try:

        gender_value = 1 if gender.get() == "Male" else 0

        age = int(umur.get())

        berat = float(bb.get())

        tinggi = float(tb.get())

        sleep_duration = float(sleep.get())

        activity_value = int(activity.get())

        steps_value = int(steps.get())

        bmi = hitung_bmi(berat, tinggi)

        bmi_category = kategori_bmi(bmi)

        hasil = prediksi(
            gender_value,
            age,
            sleep_duration,
            bmi_category,
            activity_value,
            steps_value
        )

        messagebox.showinfo(
            "Hasil Prediksi",

            f"""
Status Kesehatan

{hasil['status']}

Analisis

{hasil['analisis']}

Saran

{hasil['saran']}
"""
        )

    except Exception as e:

        messagebox.showerror(
            "Error",
            str(e)
        )


# ==========================================
# PENGATURAN TEMA
# ==========================================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# ==========================================
# WINDOW
# ==========================================

app = ctk.CTk()

app.title("Sistem Prediksi Tingkat Kesehatan Individu")

app.geometry("900x700")

app.resizable(False, False)

# ==========================================
# JUDUL
# ==========================================

judul = ctk.CTkLabel(
    app,
    text="Sistem Prediksi Tingkat Kesehatan Individu",
    font=("Arial", 28, "bold")
)

judul.pack(pady=20)

subjudul = ctk.CTkLabel(
    app,
    text="Prediksi berdasarkan pola tidur dan gaya hidup",
    font=("Arial", 16)
)

subjudul.pack()

frame = ctk.CTkFrame(
    app,
    width=800,
    height=550,
    corner_radius=15
)

frame.pack(pady=20)

frame.pack_propagate(False)

gender_label = ctk.CTkLabel(
    frame,
    text="Jenis Kelamin"
)

gender_label.pack(pady=(20,5))

gender = ctk.CTkComboBox(
    frame,
    values=[
        "Male",
        "Female"
    ]
)

gender.pack()

umur_label = ctk.CTkLabel(
    frame,
    text="Usia"
)

umur_label.pack(pady=(15,5))

umur = ctk.CTkEntry(frame)

umur.pack()

sleep_label = ctk.CTkLabel(
    frame,
    text="Durasi Tidur (Jam)"
)

sleep_label.pack(pady=(15,5))

sleep = ctk.CTkEntry(frame)

sleep.pack()

bmi_label = ctk.CTkLabel(
    frame,
    text="Berat Badan"
)

bmi_label.pack(pady=(15,5))

bb_label = ctk.CTkLabel(
    frame,
    text="Berat Badan (kg)"
)
bb_label.pack(pady=(15,5))

bb = ctk.CTkEntry(frame)
bb.pack()

tb_label = ctk.CTkLabel(
    frame,
    text="Tinggi Badan (cm)"
)
tb_label.pack(pady=(15,5))

tb = ctk.CTkEntry(frame)
tb.pack()

activity_label = ctk.CTkLabel(
    frame,
    text="Aktivitas Fisik"
)
activity_label.pack(pady=(15,5))

activity = ctk.CTkSlider(
    frame,
    from_=30,
    to=90,
    number_of_steps=60
)

activity.set(60)

activity.pack()

steps_label = ctk.CTkLabel(
    frame,
    text="Daily Steps"
)

steps_label = ctk.CTkLabel(
    frame,
    text="Daily Steps"
)
steps_label.pack(pady=(15,5))

steps = ctk.CTkSlider(
    frame,
    from_=3000,
    to=10000,
    number_of_steps=70
)

steps.set(7000)

steps.pack()

btn = ctk.CTkButton(
    frame,
    text="Prediksi",
    command=proses_prediksi
)

btn.pack(pady=30)

app.mainloop()

