from tkinter import *

window = Tk()
window.geometry("300x300")
window.title("NIET")
label = Label(window,
              text="Hello Man!",
              fg="#f542dd",
              bg="black",
              font=("Arial", 20, "bold"),
              relief=SUNKEN,
              bd=10,
              padx=10,
              pady=10)
label.pack(side="left")

window.mainloop()
