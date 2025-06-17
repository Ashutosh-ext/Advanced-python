from tkinter import *
window = Tk()
window.title("Radio Button")
window.geometry("300x300")

radio_var = BooleanVar()
radiobutton1 = Radiobutton(window, text="Male", variable=radio_var,value=False)
radiobutton2 = Radiobutton(window, text="Female", variable=radio_var,value=True)

radiobutton1.pack()
radiobutton2.pack()
window.mainloop()