import ipywidgets as widgets
from IPython.display import display, Math, clear_output

# Create interactive widgets
V_slider = widgets.FloatSlider(value=220, min=0, max=250, description='Voltage (V)')
I_slider = widgets.FloatSlider(value=2, min=0, max=4, description='Current (A)')
R_value = widgets.Label(value=f'Resistance: {R} ohms')

# Output widget for displaying formatted equations
equation_output = widgets.Output()

# Function to update the equation based on slider values
def update_equation(change):
    Pave = change['new'] * V_slider.value
    with equation_output:
        clear_output(wait=True)
        display(Math(f'P_{{ave}} = {Pave:.2f}'))

# Link the sliders with the equation update function
V_slider.observe(update_equation, names='value')
I_slider.observe(update_equation, names='value')

# Display widgets and explanation
display(widgets.VBox([V_slider, I_slider, R_value]))
display(equation_output)
