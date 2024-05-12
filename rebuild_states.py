import tkinter as tk


# Dictionary of states and their counties
states_counties = {
    "Arizona": ["Mohave", "Maricopa", "Pima"],
    "California": ["Los Angeles", "San Diego", "Oakland"],
    "Texas": ["Harris", "Travis", "Bexar"]
}

# Empty dictionary for selected locations (not used in final output)
selected_locations = {}

def update_selection_state(state, county):
    """
    Updates the selection state in state_vars based on checkbox interaction (toggle).
    """
    state_vars[state][county] = not state_vars[state][county]
    if state_vars[state][county]:  # Check if selected (True)
        county_checkbox.config(state=tk.DISABLED)  # Disable the checkbox


def submit_selection(state_vars):
    """
    Disables previously selected checkboxes and resets states for next submission.
    """
    for state, county_selections in state_vars.items():
        for county, selection_state in county_selections.items():
            county_checkbox = state_checkbox_dict[state][county]
            if selection_state:  # Check if selected (True)
                county_checkbox.config(state=tk.DISABLED)  # Disable selected checkboxes
            county_checkbox.config(state=tk.NORMAL)  # Reset state to NORMAL for all


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
    state_checkbox_dict[state] = {}
    for county in counties:
        state_vars[state][county] = 0  # Initialize as unselected (False)
        county_checkbox = tk.Checkbutton(
            root,
            text=county,
            command=lambda state=state, county=county: update_selection_state(state, county),
        )  # Update state directly on click
        county_checkbox.pack()
        state_checkbox_dict[state][county] = county_checkbox

# Submit button
submit_button = tk.Button(
    root, text="Submit Selection", command=lambda: submit_selection(state_vars)
)
submit_button.pack()

# Run the Tkinter main loop
root.mainloop()