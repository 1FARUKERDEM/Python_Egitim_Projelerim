import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("BMI calculator")
window.config(bg="blue")
window.minsize(width=350, height=300)

# --- Boy ---
label_height = tk.Label(text="Boyunuzu Giriniz => ", bg="orange", fg="black", font=("Arial", 10))
label_height.place(x=0, y=0)

entry_height_cm = tk.Entry(width=25)
entry_height_cm.place(x=150, y=4)

label_height_unit = tk.Label(text="cm", bg="blue", fg="white")
label_height_unit.place(x=310, y=4)

# --- Kilo ---
label_weight = tk.Label(text="Kilonuzu giriniz ==>>", bg="orange", fg="black", font=("Arial", 10))
label_weight.place(x=0, y=30)

entry_weight_kg = tk.Entry(width=25)
entry_weight_kg.place(x=150, y=32)

label_weight_unit = tk.Label(text="kg", bg="blue", fg="white")
label_weight_unit.place(x=310, y=35)

# --- Sonuç alanı ---
result_var = tk.StringVar(value="BMI = ")
label_result = tk.Label(textvariable=result_var, bg="blue", fg="white", font=("Arial", 11, "bold"))
label_result.place(x=90, y=95)

def bmi_category(bmi: float) -> str:
    if bmi < 18.5:
        return "Zayıf"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Fazla kilolu"
    else:
        return "Obez"

def calculate_bmi(height_cm: float, weight_kg: float) -> tuple[float, str]:
    if height_cm <= 0 or weight_kg <= 0:
        raise ValueError("Boy ve kilo pozitif olmalı.")
    m = height_cm / 100.0
    bmi = weight_kg / (m * m)
    bmi = round(bmi, 1)
    return bmi, bmi_category(bmi)

def on_click():
    try:
        h_text = entry_height_cm.get().replace(",", ".")
        w_text = entry_weight_kg.get().replace(",", ".")
        height_cm = float(h_text)
        weight_kg = float(w_text)

        bmi, cat = calculate_bmi(height_cm, weight_kg)
        result_var.set(f"BMI: {bmi}  |  Durum: {cat}")
    except ValueError:
        messagebox.showerror("Hata", "Geçerli sayı gir.\nÖrnek: Boy 178  |  Kilo 76.5")

my_button = tk.Button(text="Hesapla", bg="orange", fg="black", command=on_click, font=("Arial", 10, "italic"))
my_button.place(x=150, y=60)

window.mainloop()
