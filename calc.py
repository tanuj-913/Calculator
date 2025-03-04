import tkinter as tk
from tkinter import messagebox

def on_click(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if operation == '+':
            result.set(num1 + num2)
        elif operation == '-':
            result.set(num1 - num2)
        elif operation == '*':
            result.set(num1 * num2)
        elif operation == '/':
            if num2 == 0:
                messagebox.showerror("Error", "Division by zero is not allowed.")
                return
            result.set(num1 / num2)
        elif operation == '%':
            result.set(num1 % num2)
        elif operation == '**':
            result.set(num1 ** num2)
        elif operation == '//':
            if num2 == 0:
                messagebox.showerror("Error", "Division by zero is not allowed.")
                return
            result.set(num1 // num2)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numerical values.")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Input fields and labels
label1 = tk.Label(root, text="Enter first number:")
label1.grid(row=0, column=0, padx=10, pady=10)

entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=10)

label2 = tk.Label(root, text="Enter second number:")
label2.grid(row=1, column=0, padx=10, pady=10)

entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=10)

# Result display
result = tk.StringVar()
result_label = tk.Label(root, text="Result:")
result_label.grid(row=2, column=0, padx=10, pady=10)

result_display = tk.Label(root, textvariable=result, relief="sunken", width=15)
result_display.grid(row=2, column=1, padx=10, pady=10)

# Operation buttons
btn_add = tk.Button(root, text="+", command=lambda: on_click('+'))
btn_add.grid(row=3, column=0, padx=10, pady=10)

btn_subtract = tk.Button(root, text="-", command=lambda: on_click('-'))
btn_subtract.grid(row=3, column=1, padx=10, pady=10)

btn_multiply = tk.Button(root, text="*", command=lambda: on_click('*'))
btn_multiply.grid(row=4, column=0, padx=10, pady=10)

btn_divide = tk.Button(root, text="/", command=lambda: on_click('/'))
btn_divide.grid(row=4, column=1, padx=10, pady=10)

btn_modulo = tk.Button(root, text="%", command=lambda: on_click('%'))
btn_modulo.grid(row=5, column=0, padx=10, pady=10)

btn_power = tk.Button(root, text="^", command=lambda: on_click('**'))
btn_power.grid(row=5, column=1, padx=10, pady=10)

btn_floor_div = tk.Button(root, text="//", command=lambda: on_click('//'))
btn_floor_div.grid(row=6, column=0, padx=10, pady=10)

# Run the main loop
root.mainloop()