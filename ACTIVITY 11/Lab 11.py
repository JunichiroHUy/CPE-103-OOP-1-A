from lib2to3.pgen2.tokenize import group
from tkinter import *

window = Tk()
window.title("Using Grid Manager")
window.geometry("400x200")

txtfld1 = Entry(window, justify="center")
txtfld1.grid(row=0,column=0, padx=2, pady=2)
txtfld1.insert(END, "row 0, column 0")

txtfld2 = Entry(window, justify="center")
txtfld2.grid(row=0,column=1, padx=2, pady=2)
txtfld2.insert(END, "row 0, column 1")

txtfld3 = Entry(window, justify="center")
txtfld3.grid(row=0,column=2, padx=2, pady=2)
txtfld3.insert(END, "row 0, column 2")

yscroll = Scrollbar(window, orient=VERTICAL)
yscroll.grid(row=1, column=2, sticky="ns", padx=25)

lstbx = Listbox(window)
lstbx.grid(row=1, column=1)

for x in range(101):
    lstbx.insert(END, x)

lstbx.config(yscrollcommand = yscroll.set)
yscroll.config(command=lstbx.yview)



window.mainloop()