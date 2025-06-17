from tkinter import *

root = Tk()
root.title('Frame example')
root.geometry('800x300')

frame = Frame(root,bg='lightblue',width=200,height=100)
frame.pack()

root.mainloop()
