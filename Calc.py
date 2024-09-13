from tkinter import Tk, Entry, Button, StringVar

class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry("357x460+0+0")  # Adjusted window height to reduce extra space
        master.configure(background="gray")
        master.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ''
        Entry(width=20, background="#fff", font=('Arial', 30), textvariable=self.equation).place(x=0, y=0, height=70)

        Button(width=11, height=4, text='(', relief='flat', bg='white', command=lambda: self.show('(')).place(x=0,y=80)
        Button(width=11, height=4, text=')', relief='flat', bg='white', command=lambda: self.show(')')).place(x=90,y=80)
        Button(width=11, height=4, text='%', relief='flat', bg='white', command=lambda: self.show('%')).place(x=180,y=80)
        Button(width=11, height=4, text='1', relief='flat', bg='white', command=lambda: self.show('1')).place(x=0,y=320)
        Button(width=11, height=4, text='2', relief='flat', bg='white', command=lambda: self.show('2')).place(x=90,y=320)
        Button(width=11, height=4, text='3', relief='flat', bg='white', command=lambda: self.show('3')).place(x=180,y=320)
        Button(width=11, height=4, text='4', relief='flat', bg='white', command=lambda: self.show('4')).place(x=0,y=240)
        Button(width=11, height=4, text='5', relief='flat', bg='white', command=lambda: self.show('5')).place(x=90,y=240)
        Button(width=11, height=4, text='6', relief='flat', bg='white', command=lambda: self.show('6')).place(x=180,y=240)
        Button(width=11, height=4, text='7', relief='flat', bg='white', command=lambda: self.show('7')).place(x=0, y=160)
        Button(width=11, height=4, text='8', relief='flat', bg='white', command=lambda: self.show('8')).place(x=90, y=160)
        Button(width=11, height=4, text='9', relief='flat', bg='white', command=lambda: self.show('9')).place(x=180, y=160)
        Button(width=11, height=4, text='0', relief='flat', bg='white', command=lambda: self.show('0')).place(x=90, y=400)
        Button(width=11, height=4, text='.', relief='flat', bg='white', command=lambda: self.show('.')).place(x=180, y=400)
        Button(width=11, height=4, text='+', relief='flat', bg='white', command=lambda: self.show('+')).place(x=270, y=400)
        Button(width=11, height=4, text='-', relief='flat', bg='white', command=lambda: self.show('-')).place(x=270, y=320)
        Button(width=11, height=4, text='/', relief='flat', bg='white', command=lambda: self.show('/')).place(x=270, y=160)
        Button(width=11, height=4, text='x', relief='flat', bg='white', command=lambda: self.show('*')).place(x=270, y=240)
        Button(width=11, height=4, text='=', relief='flat', bg='#90ee90', command=self.solve).place(x=0, y=400)
        Button(width=11, height=4, text='C', relief='flat', bg='#f08080', command=self.clear).place(x=270, y=80)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            result = eval(self.entry_value)
            self.equation.set(result)
        except:
            self.equation.set("Error")


root = Tk()
calc = Calculator(root)
root.mainloop()