import tkinter as tk


# Dictionary of states and their counties
states_counties = {
    "Arizona": ["Mohave", "Maricopa", "Pima"],
    "California": ["Los Angeles", "San Diego", "Oakland"],
    "Texas": ["Harris", "Travis", "Bexar"]
}

# Selected locations dictionary (simple structure)
selected_locations = {}


def is_selected(state, county):
    """
    Checks if the given county in the specified state is selected (returns True/False).
    """
    return state_vars[state][county] == 1  # Directly check the stored value


def update_selection_state(state, county):
    """
    Updates the selection state in state_vars based on checkbox interaction (toggle).
    """
    state_vars[state][county] = not state_vars[state][county]  # Toggle selection state


def get_selected_locations():
    """
    Gets a dictionary of selected states and their counties (simple structure).
    """
    selected_locations = {}
    for state, county_selections in state_vars.items():
        for county, selection_state in county_selections.items():
            if selection_state:  # Check directly for True (selected)
                if state not in selected_locations:
                    selected_locations[state] = []  # Initialize list for counties
                selected_locations[state].append(county)  # Append selected county
    return selected_locations


def submit_selection(state_vars):
    """
    Gathers selected counties and updates the selected_locations dictionary with a simple structure.
    """
    global selected_locations
    selected_locations = get_selected_locations()  # Call the new get_selected_locations function
    print("Selected Locations:", selected_locations)


# **Move state_vars definition outside root.mainloop()**
state_vars = {}  # Dictionary to store state selection states (True/False)


# Create the main window
root = tk.Tk()
root.title("Multi-State County Selection")

# Loop through states and create selection checkboxes
for state, counties in states_counties.items():
    state_label = tk.Label(root, text=state)
    state_label.pack()

    state_vars[state] = {}
    for county in counties:
        state_vars[state][county] = 0  # Initialize as unselected (False)
        county_checkbox = tk.Checkbutton(
            root,
            text=county,
            command=lambda state=state, county=county: update_selection_state(state, county),
        )  # Update state directly on click
        county_checkbox.pack()

# Submit button
submit_button = tk.Button(
    root, text="Submit Selection", command=lambda: submit_selection(state_vars)
)
submit_button.pack()

# Run the Tkinter main loop
root.mainloop()