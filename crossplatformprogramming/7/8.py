from tkinter import *
from tkinter import scrolledtext


window = Tk()
window.title("Hello World")
window.geometry('400x250')
txt = scrolledtext.ScrolledText(window, width=40, height=10)
txt.grid(column=0, row=0)
window.mainloop()
