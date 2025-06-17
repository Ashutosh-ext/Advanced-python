from tkinter import *

from mistune.plugins.formatting import insert

window = Tk()
window.title("listbox example")
window.geometry("300x300")

listbox = Listbox(window,

                  )
listbox.insert(1,"option 1")
listbox.insert(2,"option 2")
listbox.insert(3,"option 3")
listbox.pack()
window.mainloop()
