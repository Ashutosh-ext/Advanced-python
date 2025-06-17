from tkinter import *
from tkcalendar import DateEntry
window = Tk()
window.title("Date Picker Example")
window.geometry("800x300")

date_entry = DateEntry(window)
date_entry.pack()
window.mainloop()