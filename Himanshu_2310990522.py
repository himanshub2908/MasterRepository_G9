import tkinter as tk
from math import *

def evaluate_expression():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear():
    entry.delete(0, tk.END)

def button_click(char):
    entry.insert(tk.END, char)

def square_root():
    entry.insert(tk.END, "sqrt(")

def trig_function(func):
    entry.insert(tk.END, func + "(")

root = tk.Tk()
root.title("Scientific Calculator")

entry = tk.Entry(root, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('C', 1, 4),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('(', 2, 4),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), (')', 3, 4),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3), ('^', 4, 4)
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, padx=20, pady=20, command=lambda char=text: button_click(char))
    button.grid(row=row, column=col)

button_sqrt = tk.Button(root, text='√', padx=20, pady=20, command=square_root)
button_sqrt.grid(row=5, column=0)

button_sin = tk.Button(root, text='sin', padx=20, pady=20, command=lambda: trig_function("sin"))
button_sin.grid(row=5, column=1)

button_cos = tk.Button(root, text='cos', padx=20, pady=20, command=lambda: trig_function("cos"))
button_cos.grid(row=5, column=2)

button_tan = tk.Button(root, text='tan', padx=20, pady=20, command=lambda: trig_function("tan"))
button_tan.grid(row=5, column=3)

button_clear = tk.Button(root, text='Clear', padx=20, pady=20, command=clear)
button_clear.grid(row=5, column=4)

root.mainloop()
