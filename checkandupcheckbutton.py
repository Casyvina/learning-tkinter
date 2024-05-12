import  tkinter as tk

window= tk.Tk()
# 0 for unchecked, 1 for checked
var = tk.IntVar()

def create_checkbox():
    # var = tk.IntVar()
    checkbox = tk.Checkbutton(window, text="My Checkbox", variable=var, )
    checkbox.pack()
    print(checkbox)
    return checkbox

def submit_clicked():
    # Access the checkbox store
    checked = var.get()
    print(var.get())
    
    # Process your submission logic here
    # (e.g, send data to server to unchecked)
    var.set(0)
    checkbox.config(state=tk.DISABLED)
    
# Create the checkbox
checkbox = create_checkbox()
checkbox2 = create_checkbox()

# Create the submit button
submit_button = tk.Button(window, text="Submit", command=submit_clicked)
submit_button.pack()

window.mainloop()