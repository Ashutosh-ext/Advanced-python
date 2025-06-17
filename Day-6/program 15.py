from tkinter import *
window = Tk()
window.geometry("300x300")
window.title("Check button")

check_var = BooleanVar()
checkbutton = Checkbutton(window, text="Check",variable=check_var)
checkbutton.pack()

window.mainloop()