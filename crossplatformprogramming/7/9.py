from tkinter import *
from tkinter import messagebox

def clicked():
    messagebox.showinfo('Заголовок','Текст')


window = Tk()
window.title("Hello World")
window.geometry('400x250')
btn = Button(window, text='Клик', command=clicked)
btn.grid(column=0, row=0)
window.mainloop()
