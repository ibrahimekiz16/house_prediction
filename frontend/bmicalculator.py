import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height_cm = float(entry_height.get())
        height = height_cm / 100
        bmi = weight / (height ** 2)
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obesity"
        messagebox.showinfo("Result", f"BMI: {bmi:.2f}\nCategory: {category}")
    except:
        messagebox.showerror("Error", "Please enter valid numbers.")

window = tk.Tk()
window.title("BMI Calculator")

tk.Label(window, text="Your Weight (kg):").pack()
entry_weight = tk.Entry(window)
entry_weight.pack()

tk.Label(window, text="Your Height (centimeter):").pack()
entry_height = tk.Entry(window)
entry_height.pack()

tk.Button(window, text="Calculate", command=calculate_bmi).pack()

window.mainloop()
