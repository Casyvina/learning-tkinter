import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('600x400')
window.title('Multi city')

states_counties = {
    "Arizona": ["Mohave", "Maricopa", "Pima", ],
    "California": ["Los Angeles", "San Diego", "Oakland", 'Santa Rosa', 'Orange County', 'San Diego', 'San Mateo', 'San Jose', 'Sacramento'],
    "Texas": ["Harris", "Travis", "Bexar", "Austin", "Dallas", "San Antonio", "Arlington", "Corpus Christi" ]
}

table = ttk.Treeview(window, columns = ('state', 'county'), show = 'headings')
table.heading('state', text= 'state')
table.heading('county', text='county')
table.pack()

# table.insert(parent='', index=0, values= ('Arizona', 'mohave county'))

selected_location = {}

for state, counties in states_counties.items():
    for county in counties:
        data = (state, county)
        table.insert(parent='', index=tk.END, values=data)
    
# event
def item_select(_):
    # print(table.selection())
    for i in table.selection():
        selected_state = table.item(i)['values'][0]
        print(selected_state)
        selected_county = table.item(i)['values'][1]
        # selected_locations[state].append(county)
        selected_location["state"].append(selected_state)
        selected_location["county"].append(selected_county)
    # table.item(table.selection())

# table.bind('<<TreeviewSelect>>', lambda event: print(table.selection()))
table.bind('<<TreeviewSelect>>', item_select)

button = ttk.Button(window, text='Print Selected', command=lambda: print(selected_location))

button.pack()

# items

window.mainloop()