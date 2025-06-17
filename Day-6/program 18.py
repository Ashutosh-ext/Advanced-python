from tkinter import *
from tkinter.ttk import Combobox
window = Tk()
window.title("combobox Example")
window.geometry("800x300")


def combobox_selected(event):
    selected_value = combobox.get()
    label.config(text=f"Selected value: {selected_value}")

label= Label(window, text="Select an option")
label.pack()

options = ["Option 1", "Option 2", "Option 3"]

combobox = Combobox(window, values=options)
combobox.pack(padx=20, pady=10)
combobox.bind("<<ComboboxSelected>>", combobox_selected)
window.mainloop()