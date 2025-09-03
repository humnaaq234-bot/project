import tkinter as tk
from tkinter import messagebox
def calculate_bmi():
    try:
        # Get user input
        height = float(entry_height.get())
        weight = float(entry_weight.get())

        # Formula for BMI
        bmi = weight / (height ** 2)

        # Check category
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obesity"

        # Show result
        label_result.config(text=f"Your BMI: {bmi:.1f}\nCondition: {category}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers!")

# ----------------- UI -----------------
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x250")

# Height input
tk.Label(root, text="Enter height (m):").pack(pady=5)
entry_height = tk.Entry(root)
entry_height.pack(pady=5)

# Weight input
tk.Label(root, text="Enter weight (kg):").pack(pady=5)
entry_weight = tk.Entry(root)
entry_weight.pack(pady=5)

# Button
tk.Button(root, text="Calculate BMI", command=calculate_bmi).pack(pady=10)

# Result display
label_result = tk.Label(root, text="", font=("Arial", 12, "bold"))
label_result.pack(pady=10)

# Run program
root.mainloop()
