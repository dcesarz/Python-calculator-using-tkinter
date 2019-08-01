from tkinter import *




def logger(func):
    import logging
    logging.basicConfig(filename='operations.log', level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(
            'Function {} ran with args {} &  kwargs {}. RETURNS: {} \n-----\n'.format(func.__name__, args, kwargs,
                                                                                       func(*args, **kwargs))

        )
        return func(*args, **kwargs)

    return wrapper


class CalcApp(Frame):

    @logger
    def getab(self):
        a = self.tf1.get("1.0", END)
        b = self.tf2.get("1.0", END)
        try:
            a = int(a)
            b = int(b)
        except ValueError:
            print("ERROR. Assigning values substitute values")
            a = 0
            b = 1
        return a, b

    @logger
    def multiply(self):
        a, b = self.getab()
        z = a * b
        self.resultdisplay(z)
        return z

    @logger
    def divide(self):
        a, b = self.getab()
        z = a / b
        self.resultdisplay(z)
        return z

    @logger
    def add(self):
        a, b = self.getab()
        z = a + b
        self.resultdisplay(z)
        return z

    @logger
    def subtract(self):
        a, b = self.getab()
        z = a - b
        self.resultdisplay(z)
        return z

    def resultdisplay(self, z):
        self.result.config(state=NORMAL)
        self.result.delete('1.0', END)
        self.result.insert(INSERT, z)
        self.result.config(state=DISABLED)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.winfo_toplevel().title("Calc")
        self.pack()

        self.tf1 = Text(root, height="1", width="4")
        self.tf1.config(font=("Calibri", 20))
        self.tf1.pack(padx=10, pady=10, side=LEFT)

        self.tf2 = Text(root, height="1", width="4")
        self.tf2.config(font=("Calibri", 20))
        self.tf2.pack(padx=10,pady=10, side=LEFT)

        self.result = Text(root, height="1", width="8")
        self.result.config(state=DISABLED, font=("Calibri", 20))
        self.result.pack(padx=10,pady=10, side=LEFT)

        self.addition = Button(self)
        self.addition.config(image=addimage, width="50", height="50")
        self.addition["command"] = self.add
        self.addition.pack(side=LEFT)

        self.subtraction = Button(self)
        self.subtraction.config(image=subimage, width="50", height="50")
        self.subtraction["command"] = self.subtract
        self.subtraction.pack(side=LEFT)

        self.multiplication = Button(self)
        self.multiplication.config(image=mulimage, width="50", height="50")
        self.multiplication["command"] = self.multiply
        self.multiplication.pack(side=LEFT)

        self.division = Button(self)
        self.division.config(image=divimage, width="50", height="50")
        self.division["command"] = self.divide
        self.division.pack(side=LEFT)


root = Tk()
addimage = PhotoImage(file="add.png")
subimage = PhotoImage(file="sub.png")
mulimage = PhotoImage(file="mul.png")
divimage = PhotoImage(file="div.png")
app = CalcApp(master=root)
app.mainloop()
