import tkinter as tk


# Dictionary of states and their counties
states_counties = {
    "Arizona": ["Mohave", "Maricopa", "Pima"],
    "California": ["Los Angeles", "San Diego", "Oakland"],
    "Texas": ["Harris", "Travis", "Bexar"]
}

# Selected locations dictionary
selected_locations = {}

# **Move state_vars definition outside root.mainloop()**
state_vars = {}  # Dictionary to store state variable references for each state

def get_selected_counties(state):
    """
    Gets the selected counties for a given state.
    """
    selected_counties = []
    for var in state_vars[state].values():
        if var.get() == 1:
            selected_counties.append(var.name)  # Use var.name for variable name
            print(f"Selected county in {state}: {var.name}")  # Print check state
    return selected_counties


def submit_selection(state_vars):
    """
    Gathers selected counties for each state and updates the selected_locations dictionary.
    """
    global selected_locations
    selected_locations = {}
    for state, state_vars in state_vars.items():
        selected_counties = get_selected_counties(state)
        for county in selected_counties:
            selected_locations[state] = county  # Update with each selected county

    print("Selected Locations:", selected_locations)

# Create the main window
root = tk.Tk()
root.title("Multi-State County Selection")

# Loop through states and create selection checkboxes
for state, counties in states_counties.items():
    state_label = tk.Label(root, text=state)
    state_label.pack()
    
    # create the state folder
    state_vars[state] = {}
    # loops through the country in that statelist
    for county in counties:
        var = tk.IntVar(root, value=0, name=county)  # Provide the name argument here
        county_checkbox = tk.Checkbutton(root, text=county, variable=var)
        county_checkbox.pack()
        state_vars[state][county] = var  # Store the variable object

# Submit button
submit_button = tk.Button(
    root, text="Submit Selection", command=lambda: submit_selection(state_vars)
)
submit_button.pack()

# Run the Tkinter main loop
root.mainloop()