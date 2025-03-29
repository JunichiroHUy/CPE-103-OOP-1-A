import tkinter as tk
from tkinter import ttk, PhotoImage
from tkinter import messagebox
from tkinter.messagebox import showinfo

window = tk.Tk()
window.title("combobox")
window.geometry('500x700')
window.configure(bg="#054E98")

ttk.Label(window, text="Choose your birth month", foreground = 'Black',
          font = ("Broadway", 15)).grid(row=1, column=1)

ttk.Label(window, text="Month: ",
          font=("Times New Roman", 12)).grid(column = 0,
                                             row = 5, padx = 5, pady=25)

ttk.Label(window, text="Date: ",
          font=("Times New Roman", 12)).grid(column = 0,
                                             row = 6, padx = 5, pady=25)
ttk.Label(window, text="Year: ",
          font=("Times New Roman", 12)).grid(column = 0,
                                             row = 7, padx = 5, pady=25)

def choice():
    showinfo( title= "Selection",
             message = f"Your birthday is on{n.get()} {d.get()}, {y.get()}")

    month.bind("<<ComboboxSelected>>", choice)
    day.bind("<<ComboboxSelected>>", choice)
    year.bind("<<ComboboxSelected>>", choice)

ttk.Button(window, text="Submit", command=choice,
           ).grid(column = 0,
                                             row = 10, padx = 5, pady=25)

d = tk.StringVar()
day = ttk.Combobox(window, width=27, textvariable=d)
day['values'] = tuple(str(i) for i in range (1, 32))
day.grid(column=1, row=6)
day.current()

y = tk.StringVar()
year = ttk.Combobox(window, width=27, textvariable=y)
year['values'] = tuple(str(i) for i in range (1800, 2050))
year.grid(column = 1, row=7)
year.current()


n = tk.StringVar()
month = ttk.Combobox(window, width=27, textvariable=n)

month['values'] = (' January',
                   ' Febuary',
                   ' March',
                   ' April',
                   ' May',
                   ' June',
                   ' July',
                   ' August',
                   ' September',
                   ' October',
                   ' November',
                   ' December')

month.grid(column=1, row=5)
month.current()

window.mainloop()
