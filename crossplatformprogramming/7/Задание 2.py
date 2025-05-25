from tkinter import *
window = Tk()
window.title("Hello World")
window.geometry('400x250')
lbl = Label(window, text="Привет", font=("Arial Bold", 50))
lbl.grid(column=0, row=0)
window.mainloop()

