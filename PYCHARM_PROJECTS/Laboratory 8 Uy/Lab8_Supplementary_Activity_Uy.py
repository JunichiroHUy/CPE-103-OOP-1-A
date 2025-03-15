from idlelib.configdialog import is_int
from tkinter import *
from tkinter import messagebox
import math

class MyWindow:
    def __init__(self, win):
        #Text and labels
        self.lbl1=Label(win, text='1st number (x₁)', fg="white", bg="#5A6484" )
        self.lbl1.place(x=100, y=50)
        self.t1 = Entry(bd=3)
        self.t1.place(x=200, y=50)

        self.lbl2=Label(win, text='2nd number (x₂)', fg="white", bg="#5A6484")
        self.lbl2.place(x=100, y=100)
        self.t2 = Entry(bd=3)
        self.t2.place(x=200, y=100)

        self.lbl3=Label(win, text='Result', fg="white", bg="#5A6484")
        self.lbl3.place(x=100, y=240)
        self.t3 = Entry(bd=3)
        self.t3.place(x=150, y=240)

        #buttons
        self.b1 = Button(win, text='Add', command=self.add, fg="white", bg="#5A6484")
        self.b2 = Button(win, text='Subtract', fg="white", bg="#5A6484")
        self.b2.bind('<Button-1>', self.sub)
        self.b3 = Button(win, text='Multiply', command=self.multiply, fg="white", bg="#5A6484")
        self.b4 = Button(win, text='Divide', command=self.divide, fg="white", bg="#5A6484")
        self.b5 = Button(win, text='Clear', command=self.clear, fg='white', bg="red")
        self.b1.place(x=100, y=150)
        self.b2.place(x=150, y=150)
        self.b3.place(x=220, y=150)
        self.b4.place(x=290, y=150)
        self.b5.place(x=100, y=420)

        self.b6 = Button(win, text='√', command=self.root, fg="white", bg="#5A6484")
        self.b6.place(x=100, y=200)

        self.b7 = Button(win, text='x₁ ^ x₂', command=self.power, fg="white", bg="#5A6484")
        self.b7.place(x=150, y=200)

        self.b8 = Button(win, text='Sin(x₁)', command=self.sine, fg="white", bg="#5A6484")
        self.b8.place(x=220, y=200)
        self.b9 = Button(win, text='Cos(x₁)', command=self.cos, fg="white", bg="#5A6484")
        self.b9.place(x=290, y=200)

        self.b10 = Button(win, text='Tan(x₁)', command=self.tan, fg="white", bg="#5A6484")
        self.b10.place(x=290, y=240)

        #history
        self.lbl4=Label(win, text='History', fg="white", bg="#5A6484")
        self.lbl4.place(x=100, y=280)
        self.history_show = Text(win, height= 10, width=23, bd=3)
        self.history_show.place(x=150, y=280)


    def clear(self):
        self.t1.delete(0, 'end')
        self.t2.delete(0, 'end')
        self.t3.delete(0, 'end')

    def tan(self):
        try:
            self.t3.delete(0, 'end')
            num1 = int(self.t1.get())
            result = math.tan(num1)
            self.t3.insert(END, str(result))
            self.history(f"tan({num1}) = {result}")
        except ValueError:
            messagebox.showerror("Invalid!", "You did not put a proper integer.")

    def cos(self):
        try:
            self.t3.delete(0, 'end')
            num1 = int(self.t1.get())
            result = math.cos(num1)
            self.t3.insert(END, str(result))
            self.history(f"cos({num1}) = {result}")
        except ValueError:
            messagebox.showerror("Invalid!", "You did not put a proper integer.")

    def sine(self):
        try:
            self.t3.delete(0, 'end')
            num1 = int(self.t1.get())
            result = math.sin(num1)
            self.t3.insert(END, str(result))
            self.history(f"sin({num1}) = {result}")
        except ValueError:
            messagebox.showerror("Invalid!", "You did not put a proper integer.")

    def power(self):
        try:
            self.t3.delete(0, 'end')
            num1 = int(self.t1.get())
            num2 = int(self.t2.get())
            result = num1 ** num2
            self.t3.insert(END, str(result))
            self.history(f"{num1} ^ {num2} = {result}")
        except ValueError:
            messagebox.showerror("Invalid!", "You did not put a proper integer.")

    def divide(self):

        try:
            self.t3.delete(0, 'end')
            num1 = int(self.t1.get())
            num2 = int(self.t2.get())
            result = num1 / num2
            self.t3.insert(END, str(result))
            self.history(f"{num1} / {num2} = {result}")
        except ValueError:
            messagebox.showerror("Invalid!", "You did not put a proper integer.")

    def multiply(self):
        try:
            self.t3.delete(0, 'end')
            num1 = int(self.t1.get())
            num2 = int(self.t2.get())
            result = num1 * num2
            self.t3.insert(END, str(result))
            self.history(f"{num1} x {num2} = {result}")
        except ValueError:
            messagebox.showerror("Invalid!", "You did not put a proper integer.")

    def add(self):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 + num2
        self.t3.insert(END, str(result))
        self.history(f"{num1} + {num2} = {result}")

    def sub(self, event):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 - num2
        self.t3.insert(END, str(result))
        self.history(f"{num1} - {num2} = {result}")

    def history(self, entry):
        self.history_show.insert(END, entry + '\n')

    def root(self):
        try:
            self.t3.delete(0, 'end')
            num1 = int(self.t1.get())
            result = num1 ** 0.5
            self.t3.insert(END, str(result))
            self.history(f"√{num1} = {result}")
        except ValueError:
            messagebox.showerror("Invalid!", "You did not put a proper integer.")




window = Tk()
mywin = MyWindow(window)
window.title('Basic Calculator NI CHIRO')
window.geometry("400x600+10+10")
window.configure(bg = "#C4C4DF")
window.mainloop()