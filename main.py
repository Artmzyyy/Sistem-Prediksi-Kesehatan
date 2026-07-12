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

        aktivitas_mapping = {
            "Sangat Rendah": 30,
            "Rendah": 45,
            "Sedang": 60,
            "Tinggi": 75,
            "Sangat Tinggi": 90
        }

        activity_value = aktivitas_mapping[activity.get()]
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

# ==========================================
# DUA KOLOM
# ==========================================

left_col = ctk.CTkFrame(frame, fg_color="transparent")
right_col = ctk.CTkFrame(frame, fg_color="transparent")

left_col.grid(row=0, column=0, padx=40, pady=25, sticky="n")
right_col.grid(row=0, column=1, padx=40, pady=25, sticky="n")

# --------------------------
# KOLOM KIRI
# --------------------------

ctk.CTkLabel(left_col, text="Jenis Kelamin").pack(anchor="w", pady=(0,5))

gender = ctk.CTkComboBox(
    left_col,
    values=["Male","Female"],
    width=250
)
gender.set("Male")
gender.pack()

ctk.CTkLabel(left_col, text="Usia").pack(anchor="w", pady=(15,5))

umur = ctk.CTkEntry(left_col,width=250)
umur.pack()

ctk.CTkLabel(left_col, text="Durasi Tidur (Jam)").pack(anchor="w", pady=(15,5))

sleep = ctk.CTkEntry(left_col,width=250)
sleep.pack()

# --------------------------
# KOLOM KANAN
# --------------------------

ctk.CTkLabel(right_col, text="Berat Badan (kg)").pack(anchor="w", pady=(0,5))

bb = ctk.CTkEntry(right_col,width=250)
bb.pack()

ctk.CTkLabel(right_col, text="Tinggi Badan (cm)").pack(anchor="w", pady=(15,5))

tb = ctk.CTkEntry(right_col,width=250)
tb.pack()

ctk.CTkLabel(right_col, text="Aktivitas Fisik").pack(anchor="w", pady=(15,5))

activity = ctk.CTkComboBox(
    right_col,
    values=[
        "Sangat Rendah",
        "Rendah",
        "Sedang",
        "Tinggi",
        "Sangat Tinggi"
    ],
    width=250
)

activity.set("Sedang")
activity.pack()

ctk.CTkLabel(right_col, text="Daily Steps").pack(anchor="w", pady=(15,5))

steps = ctk.CTkEntry(right_col,width=250)
steps.insert(0,"7000")
steps.pack()

# --------------------------
# TOMBOL
# --------------------------

btn_prediksi = ctk.CTkButton(
    frame,
    text="Prediksi Kesehatan",
    width=350,
    height=42,
    font=("Arial",16,"bold"),
    command=proses_prediksi
)

btn_prediksi.grid(
    row=1,
    column=0,
    columnspan=2,
    pady=(20,10)
)




app.mainloop()

