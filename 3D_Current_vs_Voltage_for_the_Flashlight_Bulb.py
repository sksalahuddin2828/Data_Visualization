import numpy as np
import plotly.express as px

R_bulb = 2.30  # Resistance of flashlight bulb in ohms
V_cell = 1.58  # Voltage of alkaline cell in volts
R_internal = 0.100  # Internal resistance of the cell in ohms

# Generate voltage values
V_cell_values = np.linspace(0.1, 3, 100)  # Voltage range from 0.1V to 3V
I_values = V_cell_values / (R_bulb + R_internal)

# Create an interactive plot
fig = px.scatter(x=V_cell_values, y=I_values, labels={'x':'Voltage (V)', 'y':'Current (A)'},
                 title='Current vs. Voltage for the Flashlight Bulb')
fig.show()
