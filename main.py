import customtkinter as ctk

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
    text="Kategori BMI"
)

bmi_label.pack(pady=(15,5))

bmi = ctk.CTkComboBox(
    frame,
    values=[
        "Normal",
        "Overweight",
        "Obese",
        "Underweight"
    ]
)

bmi.pack()

activity_label = ctk.CTkLabel(
    frame,
    text="Aktivitas Fisik"
)

activity_label.pack(pady=(15,5))

activity = ctk.CTkEntry(frame)

activity.pack()

steps_label = ctk.CTkLabel(
    frame,
    text="Daily Steps"
)

steps_label.pack(pady=(15,5))

steps = ctk.CTkEntry(frame)

steps.pack()

btn = ctk.CTkButton(
    frame,
    text="Prediksi"
)

btn.pack(pady=30)

app.mainloop()

