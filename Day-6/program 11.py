from tkinter import *

window = Tk()
window.geometry("300x300")
window.title("NIET")
def button_clicked():
    print("Button clicked!")

label = Label(window,
              text="Hello Man!",
              fg="#f542dd",
              bg="black",
              font=("Arial", 20, "bold"),
              relief=SUNKEN,
              bd=10,
              padx=10,
              pady=10)
button = Button(window,
                text="Click Me!",
                command=button_clicked)
button.pack(side="bottom")
label.pack(side="top")

window.mainloop()
