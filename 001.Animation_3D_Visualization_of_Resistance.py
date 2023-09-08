import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

# Constants
R1 = 0.0200  # Resistance of ammeter in ohms
R2 = 10.00   # Resistance of the resistor in ohms
V = 12.0     # Voltage in volts (you can change this as needed)

# Part (b): Calculate Resistance of the Combination
R_total = R1 + R2

# Part (c): Calculate Percent Decrease in Current
I1 = V / R2
I2 = V / R_total
percent_decrease_current = ((I1 - I2) / I1) * 100

# Part (d): Calculate Percent Increase in Voltage
V1 = I1 * R2
V2 = I2 * R_total
percent_increase_voltage = ((V2 - V1) / V1) * 100

# Part (f): Create an Interactive 3D Visualization (Using Plotly)
data = pd.DataFrame({
    'R1 (Ammeter Resistance)': np.linspace(0.001, 0.2, 100),  # Adjust the range as needed
    'R2 (Resistor Resistance)': np.linspace(1, 20, 100),  # Adjust the range as needed
})

data['Total Resistance'] = data['R1 (Ammeter Resistance)'] + R2

fig = px.scatter_3d(data, x='R1 (Ammeter Resistance)', y='R2 (Resistor Resistance)', z='Total Resistance',
                    labels={'Total Resistance': 'Total Resistance (R_total)'},
                    animation_frame=data.index)  # Use animation_frame to create animation frames

fig.update_traces(marker=dict(size=5), selector=dict(mode='markers'))

fig.update_layout(
    scene=dict(
        xaxis_title='R1 (Ammeter Resistance)',
        yaxis_title='R2 (Resistor Resistance)',
        zaxis_title='Total Resistance (R_total)',
    ),
    title='Interactive 3D Visualization of Resistance',
)

fig.show()

# Display results and visualizations
print("Total Resistance (R_total): {:.4f} ohms".format(R_total))
print("Percent Decrease in Current: {:.2f}%".format(percent_decrease_current))
print("Percent Increase in Voltage: {:.2f}%".format(percent_increase_voltage))
