#change button text on click
from tkinter import *
window = Tk()
window.geometry("300x300")
window.title("Hello Niet")
def button_clicked():
    button.config(text="Clicked",
                  bg="red",
                  fg="white")
button = Button(window,
                text="Click",
                command=button_clicked)
button.pack(side="bottom")
window.mainloop()