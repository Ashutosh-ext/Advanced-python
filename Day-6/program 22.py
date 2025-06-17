from tkinter import *
from tkinter import colorchooser

def choose_color():
    color_code = colorchooser.askcolor(title='Choose a color')
    print(color_code)

root = Tk()
root.title("Color Picker Example")
root.geometry("800x300")

button = Button(root, text="Choose Color", command=choose_color)
button.pack()

root.mainloop()

