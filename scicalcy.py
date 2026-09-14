import tkinter as tk
from tkinter import messagebox
import math



root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("420x650")
root.configure(bg="#1e1e1e")
root.resizable(False, False)



expression = ""
input_text = tk.StringVar()


input_frame = tk.Frame(root, bg="#1e1e1e")
input_frame.pack(pady=15)

input_field = tk.Entry(
    input_frame,
    textvariable=input_text,
    font=("Arial", 24, "bold"),
    width=20,
    bd=10,
    relief=tk.RIDGE,
    justify="right",
    bg="white",
    fg="black"
)

input_field.grid(row=0, column=0, ipady=15)



def btn_click(item):
    global expression
    expression += str(item)
    input_text.set(expression)

def btn_clear():
    global expression
    expression = ""
    input_text.set("")

def btn_equal():
    global expression

    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result

    except:
        messagebox.showerror("Error", "Invalid Input")
        expression = ""
        input_text.set("")



def square_root():
    global expression

    try:
        value = float(input_text.get())

        if value < 0:
            messagebox.showerror("Error", "Negative Number")
            return

        result = math.sqrt(value)

        input_text.set(round(result, 6))
        expression = str(result)

    except:
        messagebox.showerror("Error", "Invalid Input")


def square():
    global expression

    try:
        value = float(input_text.get())
        result = value ** 2

        input_text.set(round(result, 6))
        expression = str(result)

    except:
        messagebox.showerror("Error", "Invalid Input")


def sine():
    global expression

    try:
        value = float(input_text.get())

        result = math.sin(math.radians(value))

        input_text.set(round(result, 6))
        expression = str(result)

    except:
        messagebox.showerror("Error", "Invalid Input")


def cosine():
    global expression

    try:
        value = float(input_text.get())

        result = math.cos(math.radians(value))

        input_text.set(round(result, 6))
        expression = str(result)

    except:
        messagebox.showerror("Error", "Invalid Input")


def tangent():
    global expression

    try:
        value = float(input_text.get())

        result = math.tan(math.radians(value))

        input_text.set(round(result, 6))
        expression = str(result)

    except:
        messagebox.showerror("Error", "Invalid Input")


def logarithm():
    global expression

    try:
        value = float(input_text.get())

        if value <= 0:
            messagebox.showerror("Error", "Positive Number Only")
            return

        result = math.log10(value)

        input_text.set(round(result, 6))
        expression = str(result)

    except:
        messagebox.showerror("Error", "Invalid Input")


def pi_value():
    global expression

    expression += str(math.pi)
    input_text.set(expression)


btns_frame = tk.Frame(root, bg="#1e1e1e")
btns_frame.pack()



button_style = {
    "font": ("Arial", 12, "bold"),
    "width": 8,
    "height": 3,
    "bd": 2
}



buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:

    if text == "=":

        tk.Button(
            btns_frame,
            text=text,
            bg="orange",
            fg="white",
            command=btn_equal,
            **button_style
        ).grid(row=row, column=col, padx=5, pady=5)

    else:

        tk.Button(
            btns_frame,
            text=text,
            bg="#2d2d2d",
            fg="white",
            command=lambda txt=text: btn_click(txt),
            **button_style
        ).grid(row=row, column=col, padx=5, pady=5)



tk.Button(
    btns_frame,
    text="C",
    bg="red",
    fg="white",
    command=btn_clear,
    **button_style
).grid(row=5, column=0, padx=5, pady=5)

tk.Button(
    btns_frame,
    text="√",
    bg="#444",
    fg="white",
    command=square_root,
    **button_style
).grid(row=5, column=1, padx=5, pady=5)

tk.Button(
    btns_frame,
    text="x²",
    bg="#444",
    fg="white",
    command=square,
    **button_style
).grid(row=5, column=2, padx=5, pady=5)

tk.Button(
    btns_frame,
    text="log",
    bg="#444",
    fg="white",
    command=logarithm,
    **button_style
).grid(row=5, column=3, padx=5, pady=5)

tk.Button(
    btns_frame,
    text="sin",
    bg="#444",
    fg="white",
    command=sine,
    **button_style
).grid(row=6, column=0, padx=5, pady=5)

tk.Button(
    btns_frame,
    text="cos",
    bg="#444",
    fg="white",
    command=cosine,
    **button_style
).grid(row=6, column=1, padx=5, pady=5)

tk.Button(
    btns_frame,
    text="tan",
    bg="#444",
    fg="white",
    command=tangent,
    **button_style
).grid(row=6, column=2, padx=5, pady=5)

tk.Button(
    btns_frame,
    text="π",
    bg="#444",
    fg="white",
    command=pi_value,
    **button_style
).grid(row=6, column=3, padx=5, pady=5)



root.mainloop()