from tkinter import *

window = Tk()
window.title('Sum calculator')
window.geometry('800x200')

def calculate_sum():
    num1 = float(entry1.get())
    num2 = float(entry2.get())

    total = num1 + num2

    result_label.config(text=f"Sum: {total}")

label1 = Label(window, text="Number 1:")
label1.grid(row=0, column=0, padx=10, pady=5)

entry1 = Entry(window)
entry1.grid(row=0, column=1, padx=10, pady=5)

label2 = Label(window, text="Number 2:")
label2.grid(row=1, column=0, padx=10, pady=5)

entry2 = Entry(window)
entry2.grid(row=1, column=1, padx=10, pady=5)

submit_button = Button(window, text="Calculate Sum", command=calculate_sum)
submit_button.grid(row=2, column=0, padx=10, pady=5)

result_label = Label(window, text="Sum:")
result_label.grid(row=3, column=0, padx=10, pady=5)

window.mainloop()