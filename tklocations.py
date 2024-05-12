import tkinter as tk

locations = {
    "Arizona": "Mohave county",
    "California": "Oakland/East bay"
}

root = tk.Tk()
root.title("List of Locations")

listbox = tk.Listbox(root)
listbox.pack()

for state, county in locations.items():
    listbox.insert(tk.END, state)

root.mainloop()