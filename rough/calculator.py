import tkinter as tk
from tkinter import font

# ------------ basic calculator logic ------------ #
current = "0"
last = None
op = None
reset_next = False

def update_display():
    display_var.set(current)

def press_digit(d):
    global current, reset_next
    if reset_next or current == "0":
        current = str(d)
        reset_next = False
    else:
        current += str(d)
    update_display()

def press_dot():
    global current, reset_next
    if reset_next:
        current = "0."
        reset_next = False
    elif "." not in current:
        current += "."
    update_display()

def clear_all():
    global current, last, op, reset_next
    current = "0"
    last = None
    op = None
    reset_next = False
    update_display()

def plus_minus():
    global current
    if current.startswith("-"):
        current = current[1:]
    else:
        if current != "0":
            current = "-" + current
    update_display()

def percent():
    global current
    try:
        val = float(current) / 100.0
        current = str(val)
    except:
        current = "0"
    update_display()

def set_op(new_op):
    global current, last, op, reset_next
    try:
        last = float(current)
    except:
        last = 0.0
    op = new_op
    reset_next = True

def equal():
    global current, last, op, reset_next
    if op is None or last is None:
        return
    try:
        now = float(current)
        if op == "+":
            res = last + now
        elif op == "-":
            res = last - now
        elif op == "×":
            res = last * now
        elif op == "÷":
            if now == 0:
                current = "Error"
                op = None
                last = None
                reset_next = True
                update_display()
                return
            res = last / now
        current = str(res).rstrip("0").rstrip(".") if "." in str(res) else str(res)
    except:
        current = "Error"
    op = None
    last = None
    reset_next = True
    update_display()

# ------------ UI setup (iPhone-like) ------------ #
root = tk.Tk()
root.title("iPhone Style Calculator")

# fixed small window like phone
root.resizable(False, False)
root.configure(bg="black")

# custom font similar to iOS
display_font = font.Font(family="SF Pro Display", size=32, weight="bold")
btn_font = font.Font(family="SF Pro Text", size=18)

display_var = tk.StringVar(value="0")

display = tk.Label(
    root,
    textvariable=display_var,
    anchor="e",
    bg="black",
    fg="white",
    padx=16,
    pady=20,
    font=display_font
)
display.grid(row=0, column=0, columnspan=4, sticky="nsew")

# button styling helpers
def make_btn(text, row, col, bg, fg="white", cmd=None, colspan=1):
    b = tk.Button(
        root,
        text=text,
        bg=bg,
        fg=fg,
        activebackground=bg,
        activeforeground=fg,
        bd=0,
        font=btn_font,
        command=cmd
    )
    b.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=4, pady=4)
    return b

# iOS style colors (approx)
gray_btn = "#a5a5a5"
dark_btn = "#333333"
orange_btn = "#ff9500"

# first row: AC  +/-  %  ÷
make_btn("AC", 1, 0, gray_btn, "black", clear_all)
make_btn("+/-", 1, 1, gray_btn, "black", plus_minus)
make_btn("%", 1, 2, gray_btn, "black", percent)
make_btn("÷", 1, 3, orange_btn, "white", lambda: set_op("÷"))

# second row: 7 8 9 ×
make_btn("7", 2, 0, dark_btn, cmd=lambda: press_digit(7))
make_btn("8", 2, 1, dark_btn, cmd=lambda: press_digit(8))
make_btn("9", 2, 2, dark_btn, cmd=lambda: press_digit(9))
make_btn("×", 2, 3, orange_btn, "white", lambda: set_op("×"))

# third row: 4 5 6 -
make_btn("4", 3, 0, dark_btn, cmd=lambda: press_digit(4))
make_btn("5", 3, 1, dark_btn, cmd=lambda: press_digit(5))
make_btn("6", 3, 2, dark_btn, cmd=lambda: press_digit(6))
make_btn("-", 3, 3, orange_btn, "white", lambda: set_op("-"))

# fourth row: 1 2 3 +
make_btn("1", 4, 0, dark_btn, cmd=lambda: press_digit(1))
make_btn("2", 4, 1, dark_btn, cmd=lambda: press_digit(2))
make_btn("3", 4, 2, dark_btn, cmd=lambda: press_digit(3))
make_btn("+", 4, 3, orange_btn, "white", lambda: set_op("+"))

# fifth row: 0 (wide)  .   =
make_btn("0", 5, 0, dark_btn, cmd=lambda: press_digit(0), colspan=2)
make_btn(".", 5, 2, dark_btn, cmd=press_dot)
make_btn("=", 5, 3, orange_btn, "white", equal)

# make grid cells expand evenly
for i in range(6):
    root.rowconfigure(i, weight=1)
for j in range(4):
    root.columnconfigure(j, weight=1)

root.mainloop()
