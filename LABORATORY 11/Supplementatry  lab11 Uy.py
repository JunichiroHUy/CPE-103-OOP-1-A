import tkinter as tk
import math

def evaluate_expression():
    try:
        expression = entry.get()

        if 'sin' in expression or 'cos' in expression:
           result = eval(expression, {"__builtins__": None}, vars(math))
        else:
            result = str(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear_entry(event=None):
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=40, borderwidth=5, font=("Arial", 14))
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('sin', 5, 0), ('cos', 5, 1), ('^', 5, 2), ('C', 5, 3),
    ('(', 6, 0), (')', 6, 2)
]

for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, width=10, height=2, font=("Arial", 14),
                           command=evaluate_expression)
    elif text == 'C':
        button = tk.Button(root, text=text, width=10, height=2, font=("Arial", 14),
                           command=clear_entry)
    elif text == '(' or text == ')':
        button = tk.Button(root, text=text, width=10, height=2, font=("Arial", 14),
                           command=lambda t=text: entry.insert(tk.END, t))
        button.grid(row=row, column=col, pady=5, padx=5, columnspan=2, sticky='nsew')

    else:
        button = tk.Button(root, text=text, width=10, height=2, font=("Arial", 14),
                           command=lambda t=text: entry.insert(tk.END, t))
    button.grid(row=row, column=col, padx=5, pady=5)

menu_bar = tk.Menu(root)

edit_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Clear", command=clear_entry)

root.config(menu=menu_bar)

root.bind('<Return>', lambda event: evaluate_expression())

root.mainloop()
