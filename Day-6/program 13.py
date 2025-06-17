import tkinter as tk
window=tk.Tk()
window.geometry("800x200")
window.title("Scale example")

scale = tk.Scale(window,
                 from_=0,
                 to=100,
                 orient=tk.VERTICAL,
                 label="Scale",
                 )
scale.pack()
window.mainloop()