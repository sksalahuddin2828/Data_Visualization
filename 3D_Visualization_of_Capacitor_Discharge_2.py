import numpy as np
import plotly.graph_objs as go

# Define parameters
initial_voltages = np.linspace(100, 1000, 10)  # Vary initial voltage from 100 to 1000 V
capacitances = np.linspace(0.001, 0.01, 10)  # Vary capacitance from 0.001 to 0.01 F
time_constant = 1000.0  # Fixed time constant (for demonstration)

# Create a grid of values for initial voltage and capacitance
initial_voltages, capacitances = np.meshgrid(initial_voltages, capacitances)

# Calculate voltage across the capacitor for different combinations
voltage = initial_voltages * np.exp(-time_constant / (capacitances * initial_voltages))

# Create a 3D surface plot
surface = go.Surface(x=initial_voltages, y=capacitances, z=voltage, colorscale='Viridis')
layout = go.Layout(scene=dict(xaxis_title='Initial Voltage (V)', yaxis_title='Capacitance (F)', zaxis_title='Voltage (V)'),
                   title='3D Visualization of Capacitor Discharge')
fig = go.Figure(data=[surface], layout=layout)

# Show the 3D visualization
fig.show()
