import tkinter as tk
from tkinter import ttk

def button_func():
    # get the content of the entry
    entry_text = entry.get()
    label['text'] = entry_text
    entry['state'] = 'disabled'
    # print(label.configure())
    
def button_func2():
    entry_text = entry.get()
    entry['state'] = 'enabled'
    label['text'] = entry_text

# window
window = tk.Tk()
window.title('Learning tk')

# widgets
label = ttk.Label(master=window, text= 'some text')
label.pack()

entry = ttk.Entry(master=window)
entry.pack()

button = ttk.Button(master=window, text='The button', command=button_func)
button.pack()

button2 = ttk.Button(master=window, text='return button', command=button_func2)
button2.pack()
# run
window.mainloop()