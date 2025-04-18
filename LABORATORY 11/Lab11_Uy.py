import tkinter as tk
import math

def solve():
    expression = entry.get()
    try:
        result = str(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear():
    entry.delete(0, tk.END)

root = tk.Tk()
root.title('Wala')
root.geometry("350x525")
root.resizable(False, False)
root.configure(bg='lightblue')


boldfont = ("Ariel", 14, "bold")

entry = tk.Entry(root, borderwidth=10, font=("Arial", 30))
entry.grid(row=0, column=0, columnspan=4, pady=2, sticky='nsew')

clearbtn = tk.Button(root, width=40, height=3, command=clear, font=("Arial", 14, "bold"), text="C")
clearbtn.grid(row=1, column=0, columnspan=4, sticky='nsew')

row5_frame = tk.Frame(root)
row5_frame.grid(row=5, column=0, columnspan=4, sticky="nsew", padx=1, pady=3)


buttons = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
    ('0', 5, 0), ('.', 5, 1), ('+', 5, 2),
    ('=', 6, 0)

]

for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, height=3, font=boldfont,
                           command=solve)
        button.grid(row=row, column=col, columnspan=4, pady=3, sticky='nsew')

    elif text in ['0', '.', '+']:
        button = tk.Button(row5_frame, text=text, height=3, font=boldfont,
                           command=lambda t=text: entry.insert(tk.END, t))
        button.pack(side='left', expand = True, fill='both')
    else:
        button = tk.Button(root, text=text, height=3, font=boldfont,
                           command=lambda t=text: entry.insert(tk.END, t))
        button.grid(row=row, column=col, pady = 3, padx=1,  sticky='nsew')
for col in range(4):
    root.grid_columnconfigure(col, weight=1)
root.mainloop()