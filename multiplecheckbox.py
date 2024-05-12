import tkinter as tk

root = tk.Tk()

checkbox_vars = []  # Empty list to store IntVar objects


class CheckboxWrapper:
    def __init__(self, text):
        self.var = tk.IntVar(name=text)
        self.checkbox = tk.Checkbutton(root, text=text, variable=self.var)
        self.checkbox.pack()
        self.submitted = False

    def get_state(self):
        return self.var.get()

    def get_text(self):
        return self.checkbox['text']

    def set_unchecked(self):  # New method to set the checkbox to unchecked (value 0)
        self.var.set(0)
        self.checkbox.config(state=tk.NORMAL)  # Ensure checkbox is enabled for unchecking
        
    def disable_on_click(self):
        # Disable both the checkbox and the submit button after any click
        self.checkbox.config(state=tk.DISABLED)
        # submit_button.config(state=DISABLED)


class NamedIntVar(tk.IntVar):
    def __init__(self, name=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        
    def __str__(self):
        return f"NamedIntVar(name='{self.name}', value={self.get()})"

def create_checkbox(text):
    var = tk.IntVar(name=text, ) # create a separate IntVar for each checkbox
    checkbox = tk.Checkbutton(root, text=text, variable=var)
    checkbox.pack()
    checkbox_vars.append(checkbox) # Add the created IntVar to the list
    print(checkbox)
    return None # Return the variable for later access

checkbox_objects = []

for option in ["Option 1", "Option 2", "Option 3"]:
    # checkbox_vars.append(create_checkbox(option))
    checkbox_objects.append(CheckboxWrapper(option))
    
def submit_clicked():
    # Access the state of each checkbox using the list
    # for checkbox in checkbox_vars:
    #     var = checkbox["variable"]
    #     if var.get() == 1:
    #         print(f"Checkbox '{checkbox['text']}' is checked")
    global submitted
    submitted = True
    for checkbox_obj in checkbox_objects:
        if checkbox_obj.get_state() == 1:
            print(f"Checkbox '{checkbox_obj.get_text()}' is checked")
            checkbox_obj.set_unchecked()       
            checkbox_obj.disable_on_click()

def reset_checkboxes():
    for checkbox_obj in checkbox_objects:
        checkbox_obj.set_unchecked()
        # checkbox_obj.checkbox.config(state=tk.Normal)
            
submit_button = tk.Button(root, text="Submit", command=submit_clicked)
submit_button.pack()

reset_button = tk.Button(root, text="Reset Checkboxes", command=reset_checkboxes)
reset_button.pack()

root.mainloop()

