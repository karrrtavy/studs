from tkinter import *
from tkinter.ttk import Radiobutton

def clicked():
    lbl.configure(text=selected.get())

window = Tk()
window.title("Hello World")
window.geometry('400x250')
selected = IntVar()
rad1 = Radiobutton(window, text='Первый', value=1, variable=selected)
rad2 = Radiobutton(window, text='Второй', value=2, variable=selected)
rad3 = Radiobutton(window, text='Третий', value=3, variable=selected)
btn = Button(window, text="Клик", command=clicked)
lbl = Label(window)
rad1.grid(column=0, row=0)
rad2.grid(column=1, row=0)
rad3.grid(column=2, row=0)
btn.grid(column=3, row=0)
lbl.grid(column=0, row=1)
window.mainloop()
