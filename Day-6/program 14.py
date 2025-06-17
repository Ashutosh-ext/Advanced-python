from tkinter import *
window = Tk()
window.title("Spinbox Example")
window.geometry("300x300")

spinbox = Spinbox(window, from_=1, to=10)
spinbox.pack()
window.mainloop()