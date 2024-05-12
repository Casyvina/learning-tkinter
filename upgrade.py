import tkinter as tk

# Dictionary of states and their counties
states_counties = {
    "Arizona": ["Mohave", "Maricopa", "Pima"],
    "California": ["Los Angeles", "San Diego", "Oakland"],
    "Texas": ["Harris", "Travis", "Bexar"]
}

# Selected locations dictionary (simple structure)
selected_locations = {}


class StateCheckboxWrapper:
    def __init__(self, state_name, root):
        self.state_name = state_name
        self.county_checkboxes = {}  # Dictionary to store county CheckboxWrapper objects
        self.submit_button_disabled = False  # Flag to track submit button state

        # Create state label
        self.state_label = tk.Label(root, text=state_name)
        self.state_label.pack()

        # Loop through counties and create checkboxes using CheckboxWrapper
        for county in states_counties[state_name]:
            checkbox_obj = CheckboxWrapper(county, root, self)  # Pass self for submit button disable
            self.county_checkboxes[county] = checkbox_obj

    def get_selected_counties(self):
        """
        Returns a list of selected counties for this state.
        """
        selected_counties = []
        for county, checkbox_obj in self.county_checkboxes.items():
            if checkbox_obj.get_state() == 1:
                selected_counties.append(county)
        return selected_counties

    def reset(self):
        """
        Resets all county checkboxes and enables the submit button.
        """
        for checkbox_obj in self.county_checkboxes.values():
            checkbox_obj.set_unchecked()
            checkbox_obj.checkbox.config(state=tk.NORMAL)  # Ensure checkboxes are enabled
        self.submit_button_disabled = False
        submit_button.config(state=tk.NORMAL)  # Enable submit button again

class CheckboxWrapper:
    def __init__(self, text, root, state_wrapper_obj):
        self.var = tk.IntVar(name=text)
        self.checkbox = tk.Checkbutton(root, text=text, variable=self.var)
        self.checkbox.pack()
        self.state_wrapper = state_wrapper_obj  # Reference to StateCheckboxWrapper object

    def get_state(self):
        return self.var.get()

    def get_text(self):
        return self.checkbox['text']

    def set_unchecked(self):  # New method to set the checkbox to unchecked (value 0)
        self.var.set(0)
        self.checkbox.config(state=tk.NORMAL)  # Ensure checkbox is enabled for unchecking

    def disable_on_click(self):
        self.checkbox.config(state=tk.DISABLED)
        if not self.state_wrapper.submit_button_disabled:
            # Disable submit button only on the first click of any checkbox
            self.state_

def submit_selection(state_wrapper_objects):
    """
    Gathers selected counties and updates the selected_locations dictionary with a simple structure.
    """
    global selected_locations
    selected_locations = {}
    for wrapper_obj in state_wrapper_objects:
        state_name = wrapper_obj.state_name
        selected_counties = wrapper_obj.get_selected_counties()
        if selected_counties:
            selected_locations[state_name] = selected_counties
    print("Selected Locations:", selected_locations)
    


# Create the main window
root = tk.Tk()
root.title("Multi-State County Selection")

# Create StateCheckboxWrapper objects
state_wrapper_objects = []
for state_name in states_counties:
    state_wrapper = StateCheckboxWrapper(state_name, root)
    state_wrapper_objects.append(state_wrapper)

# Submit button
submit_button = tk.Button(
    root, text="Submit Selection", command=lambda: submit_selection(state_wrapper_objects)
)
submit_button.pack()

# Reset button
reset_button = tk.Button(root, text="Reset Checkboxes", command=lambda: [wrapper.reset() for wrapper in state_wrapper_objects])
reset_button.pack()

# Run the Tkinter main loop
root.mainloop()
