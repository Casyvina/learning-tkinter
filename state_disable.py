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
    Updates the selection state in state_vars based on checkbox interaction (toggle) and disables the checkbox if selected.
    """
    state_vars[state][county] = not state_vars[state][county]  # Toggle selection state
    if state_vars[state][county]:  # Check if selected (True)
        county_checkbox.config(state=tk.DISABLED)  # Disable the checkbox


def get_selected_locations():
    """
    Updates the selected_locations dictionary with selected states and their counties (simple structure).
    """
    for state, county_selections in state_vars.items():
        for county, selection_state in county_selections.items():
            if selection_state:  # Check directly for True (selected)
                if state not in selected_locations:
                    selected_locations[state] = []  # Initialize list for counties
                selected_locations[state].append(county)


def submit_selection(state_vars):
    """
    Updates the selected_locations dictionary and disables checkboxes for selected counties.
    """
    get_selected_locations()  # Update selected_locations (optional, avoids recalculation)
    for state, county_selections in state_vars.items():
        for county, selection_state in county_selections.items():
            county_checkbox = state_checkbox_dict[state][county]  # Access checkbox using dictionary
            county_checkbox.config(state=tk.NORMAL if not selection_state else tk.DISABLED)


# **Move state_vars definition outside root.mainloop()**
state_vars = {}  # Dictionary to store state selection states (True/False)

# Dictionary to store checkbox references for easy access during state updates
state_checkbox_dict = {}


# Create the main window
root = tk.Tk()
root.title("Multi-State County Selection")

# Loop through states and create selection checkboxes
for state, counties in states_counties.items():
    state_label = tk.Label(root, text=state)
    state_label.pack()

    state_vars[state] = {}
    state_checkbox_dict[state] = {}  # Initialize dictionary for checkboxes in this state
    for county in counties:
        state_vars[state][county] = 0  # Initialize as unselected (False)
        county_checkbox = tk.Checkbutton(
            root,
            text=county,
            command=lambda state=state, county=county: update_selection_state(state, county),
        )  # Update state directly on click
        county_checkbox.pack()
        state_checkbox_dict[state][county] = county_checkbox  # Store checkbox reference

# Submit button
submit_button = tk.Button(
    root, text="Submit Selection", command=lambda: submit_selection(state_vars)
)
submit_button.pack()

# Run the Tkinter main loop
root.mainloop()