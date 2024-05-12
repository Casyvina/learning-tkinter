import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Layout intro')
window.geometry('400x600')

# Top frame
top_frame = ttk.Frame(window)
label1 = ttk.Label(top_frame, text = 'Label 1', background='red')
label2 = ttk.Label(top_frame, text= 'Label 2', background='blue')


label3 = ttk.Label(window, text= 'Another labels', background='green')

# botton frame
button_frame = ttk.Frame(window)
label4 = ttk.Label(button_frame, text= 'Last of the labels', background='orange')
button = ttk.Button(button_frame, text='Button')
button2 = ttk.Button(button_frame, text='Another Button')

# side button
side_button_frame = ttk.Frame(button_frame)
button3 = ttk.Button(side_button_frame, text='Button 3')
button4 = ttk.Button(side_button_frame, text='Button 4')
button5 = ttk.Button(side_button_frame, text='Button 5')

#  top layout
label1.pack(side='left', fill = 'both', expand=True)
label2.pack(side='left', fill = 'both', expand=True)
top_frame.pack(fill = 'both', expand=True)

# middel layout
label3.pack(expand=True)

# button layout
button.pack(side='left', expand=True, fill = 'both')
label4.pack(side='left', expand=True, fill = 'both')
button2.pack(side='left', expand=True, fill = 'both')
button_frame.pack(expand=True, fill = 'both', padx=20, pady=20)

# side button layout
button3.pack(side='top', expand=True, fill='both')
button4.pack(side='top', expand=True, fill='both')
button5.pack(side='top', expand=True, fill='both')
side_button_frame.pack(side='left', expand=True, fill = 'both', padx=5)


window.mainloop()