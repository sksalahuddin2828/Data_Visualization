import numpy as np
import plotly.express as px

# Constants
R_bulb = 2.30  # Resistance of flashlight bulb in ohms
V_cell_values = np.linspace(0.1, 3, 100)  # Voltage range from 0.1V to 3V
R_internal = 0.100  # Internal resistance of the cell in ohms

# Calculate current
I_values = V_cell_values / (R_bulb + R_internal)

# Create an interactive current vs. voltage plot using Plotly
fig = px.scatter(x=V_cell_values, y=I_values, labels={'x':'Voltage (V)', 'y':'Current (A)'},
                 title='Current vs. Voltage for the Flashlight Bulb')
fig.show()

# Add mathematical equations using LaTeX
from IPython.display import display, Math

eq1 = r'I = \frac{V}{R_{\text{total}}} = \frac{V}{R_{\text{bulb}} + R_{\text{internal}}}'
display(Math(eq1))

# Add text and explanations
print("In this project, we analyze the behavior of a flashlight bulb powered by an alkaline cell.")
print("We calculate the current and visualize it as a function of voltage.")
print("The current is determined by the total resistance, which includes the bulb and internal resistance of the cell.")
