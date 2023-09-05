import numpy as np
import plotly.express as px

# Constants
R_bulb = 2.30  # Resistance of flashlight bulb in ohms
V_cell_values = np.linspace(0.1, 3, 100)  # Voltage range from 0.1V to 3V
R_internal = 0.100  # Internal resistance of the cell in ohms

# Calculate current, power, and resistance
I_values = V_cell_values / (R_bulb + R_internal)
P_values = I_values**2 * R_bulb
R_total_values = V_cell_values / I_values

# Create interactive plots
fig_current = px.scatter(x=V_cell_values, y=I_values, labels={'x':'Voltage (V)', 'y':'Current (A)'},
                         title='Current vs. Voltage for the Flashlight Bulb')
fig_power = px.scatter(x=V_cell_values, y=P_values, labels={'x':'Voltage (V)', 'y':'Power (W)'},
                       title='Power vs. Voltage for the Flashlight Bulb')
fig_resistance = px.scatter(x=V_cell_values, y=R_total_values, labels={'x':'Voltage (V)', 'y':'Total Resistance (Ω)'},
                            title='Total Resistance vs. Voltage for the Flashlight Bulb')

fig_current.show()
fig_power.show()
fig_resistance.show()

# Mathematical equations and explanations
from IPython.display import display, Math

eq1 = r'I = \frac{V}{R_{\text{total}}} = \frac{V}{R_{\text{bulb}} + R_{\text{internal}}}'
eq2 = r'P = I^2 \cdot R_{\text{bulb}}'
eq3 = r'R_{\text{total}} = \frac{V}{I}'

display(Math(eq1))
display(Math(eq2))
display(Math(eq3))

print("In this project, we analyze the behavior of a flashlight bulb powered by an alkaline cell.")
print("We calculate the current, power, and total resistance as functions of voltage.")
print("Current is determined by the total resistance, while power is given by P = I^2 * R_bulb.")
print("The total resistance is calculated as the ratio of voltage to current.")
