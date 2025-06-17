from tkinter import *
window = Tk()
window.title("Login Example")

def submit_clicked():
    result_label.config(text="Good Job!")

username_label = Label(window, text="Username:")
username_label.grid(row=0,
                    column=0,
                    padx=10,
                    pady=5)

username_entry = Entry(window)
username_entry.grid(row=0,column=1,padx=10,pady=5)

password_label = Label(window, text="Password:")
password_label.grid(row=1,column=0,padx=10,pady=5)

password_entry = Entry(window,show="*")
password_entry.grid(row=1,column=1,padx=10,pady=5)

result_label = Label(text="")
result_label.grid(row=2,column=0,padx=10,pady=5)

submit_button = Button(window, text="Submit", command=submit_clicked)
submit_button.grid(row=3,column=0,columnspan=2,pady=20)

window.mainloop()