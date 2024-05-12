import tkinter as tk
from tkinter import ttk

def button_func():
    print(string_var.get())


window = tk.Tk()
window.title('Tkinter Variables')

# tkinter variable
string_var = tk.StringVar(value='test')

label = ttk.Label(master=window, text='label', textvariable= string_var)
label.pack()

entry = ttk.Entry(master=window, textvariable=string_var)
entry.pack()


button = ttk.Button(master=window, text='button', command=button_func)
button.pack()

exercise_var = tk.StringVar(value='test')
# exercise_var.set('test')

entry1 = ttk.Entry(master=window, textvariable= exercise_var)
entry1.pack()
entry2 = ttk.Entry(master=window, textvariable= exercise_var)
entry2.pack()

label2 = ttk.Label(master=window, text='label', textvariable=exercise_var)
label2.pack()

window.mainloop()