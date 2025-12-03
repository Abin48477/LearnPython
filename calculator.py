import tkinter as tk

# Create window
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("300x300")

# Entry box
entry = tk.Entry(window, width=20, font=("Arial", 18))
entry.pack(pady=20)

# Function to calculate
def calculate(op):
    try:
        num1 = float(entry.get())
        global last_number
        last_number = num1
        entry.delete(0, tk.END)
        entry.insert(0, op)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def equal():
    try:
        expression = str(last_number) + entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Buttons
btn_add = tk.Button(window, text="+", width=10, command=lambda: calculate("+"))
btn_sub = tk.Button(window, text="-", width=10, command=lambda: calculate("-"))
btn_mul = tk.Button(window, text="*", width=10, command=lambda: calculate("*"))
btn_div = tk.Button(window, text="/", width=10, command=lambda: calculate("/"))
btn_equal = tk.Button(window, text="=", width=10, command=equal)

btn_add.pack()
btn_sub.pack()
btn_mul.pack()
btn_div.pack()
btn_equal.pack()

window.mainloop()
