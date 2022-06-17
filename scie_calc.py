from tkinter import *
from tkinter import Tk
from tkinter import StringVar, Entry, Button
from math import sin, cos, tan, asin, acos, atan, asinh, acosh, atanh, pi, e, radians, degrees

window = Tk()
window.title('Scientific Calculator')
window.configure(background="light blue", bd=20, relief=RIDGE)
window.resizable(False, False)


class Calculator:
    def __init__(self):
        self.string = StringVar()

        entry = Entry(window, textvariable=self.string, bd=10, font="Arial")
        entry.grid(row=0, column=0, columnspan=6)
        entry.configure(background="light green")
        entry.focus()

        values = ["sin", "cos", "tan", "(", ")",
                  "asin", "acos", "atan", "pi", "e",
                  "asinh", "acosh", "atanh", "radians", "degrees",
                  "7", "8", "9", "DEL", "AC",
                  "4", "5", "6", "*", "/",
                  "1", "2", "3", "+", "-",
                  "0", ".", "="]

        i = 0
        row = 1
        col = 0

        for txt in values:
            padx = 10
            pady = 10
            if i == 5:
                row = 2
                col = 0
            if i == 10:
                row = 3
                col = 0
            if i == 15:
                row = 4
                col = 0
            if i == 20:
                row = 5
                col = 0
            if i == 25:
                row = 6
                col = 0
            if i == 30:
                row = 7
                col = 0
            if txt == '=':
                btn = Button(window, bd=5, height=2, width=4, padx=65, pady=pady, text=txt,
                             command=lambda txt=txt: self.equals())
                btn.grid(row=row, column=col, padx=1, pady=1, columnspan=3)
                btn.configure(background="orange")
            elif txt == 'DEL':
                btn = Button(window, bd=5, height=2, width=4, padx=padx, pady=pady, text=txt,
                             command=lambda txt=txt: self.delete())
                btn.grid(row=row, column=col, padx=1, pady=1)
                btn.configure(background="orange")
            elif txt == 'AC':
                btn = Button(window, bd=5, height=2, width=4, padx=padx, pady=pady, text=txt,
                             command=lambda txt=txt: self.clearall())
                btn.grid(row=row, column=col, padx=1, pady=1)
                btn.configure(background="orange")
            elif txt == 'pi':
                btn = Button(window, bd=5, height=2, width=4, padx=padx, pady=pady, text="π",
                             command=lambda txt=txt: self.addchar(txt))
                btn.grid(row=row, column=col, padx=1, pady=1)
                btn.configure(background="grey")
            elif txt == 'radians':
                btn = Button(window, bd=5, height=2, width=4, padx=padx, pady=pady, text="Rad",
                             command=lambda txt=txt: self.addchar(txt))
                btn.grid(row=row, column=col, padx=1, pady=1)
                btn.configure(background="grey")
            elif txt == 'degrees':
                btn = Button(window, bd=5, height=2, width=4, padx=padx, pady=pady, text="Deg",
                             command=lambda txt=txt: self.addchar(txt))
                btn.grid(row=row, column=col, padx=1, pady=1)
                btn.configure(background="grey")
            elif txt == '/':
                btn = Button(window, bd=5, height=2, width=4, padx=padx, pady=pady, text="÷",
                             command=lambda txt=txt: self.addchar(txt))
                btn.grid(row=row, column=col, padx=1, pady=1)
                btn.configure(background="white")
            elif i < 15:
                btn = Button(window, bd=5, height=2, width=4, padx=padx, pady=pady, text=txt,
                             command=lambda txt=txt: self.addchar(txt))
                btn.grid(row=row, column=col, padx=1, pady=1)
                btn.configure(background="grey")
            else:
                btn = Button(window, bd=5, height=2, width=4, padx=padx, pady=pady, text=txt,
                             command=lambda txt=txt: self.addchar(txt))
                btn.grid(row=row, column=col, padx=1, pady=1)
                btn.configure(background="white")

            col = col + 1
            i = i + 1
        window.mainloop()

    def clearall(self):
        self.string.set("")

    def equals(self):
        result = ""
        try:
            result = eval(self.string.get())
            self.string.set(result)
        except:
            result = "INVALID INPUT"
        self.string.set(result)

    def addchar(self, char):
        self.string.set(self.string.get() + (str(char)))

    def delete(self):
        self.string.set(self.string.get()[0:-1])


Calculator()
