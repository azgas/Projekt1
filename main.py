from tkinter import *

window = Tk()
window.title("Welcome")
window.geometry('350x200')
lbl = Label(window, text="Hello", font=("Arial Bold", 50))
lbl.grid(column=0, row=0)
btn = Button(window, text="click")
btn.grid(column=1, row=0)
window.mainloop()