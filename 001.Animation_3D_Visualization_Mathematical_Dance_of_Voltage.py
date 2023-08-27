import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import sympy as sp

# Given peak voltage
peak_voltage = 679

# Calculate the RMS voltage using numpy
rms_voltage = peak_voltage / np.sqrt(2)

# Display the RMS voltage
print(f"RMS Voltage: {rms_voltage:.2f} V")

# Create symbolic variable for visualization
t = sp.symbols('t')

# Create a sinusoidal equation for visualization
equation = peak_voltage * sp.sin(t)

# Convert sympy expression to numpy function
equation_numpy = sp.lambdify(t, equation, "numpy")

# Generate time values for animation
time_vals = np.linspace(0, 2 * np.pi, 100)

# Generate data for each time step
data = []
for t_val in time_vals:
    voltage_val = equation_numpy(t_val)
    data.append({'Time': t_val, 'Voltage': voltage_val})

# Create a DataFrame
df = pd.DataFrame(data)

# Create animated 3D visualization using Plotly
fig = px.scatter_3d(df, x='Time', y='Voltage', z='Time',
                    animation_frame='Time', color='Voltage',
                    title='Mathematical Dance of Voltage',
                    labels={'Time': 'Time', 'Voltage': 'Voltage'})

# Set color scale for voltage
fig.update_traces(marker=dict(size=5),
                  selector=dict(mode='markers'))

# Customize layout
fig.update_layout(scene=dict(
                    xaxis_title='Time',
                    yaxis_title='Voltage',
                    zaxis_title='Time'),
                  scene_camera=dict(up=dict(x=0, y=0, z=1),
                                    eye=dict(x=-1.5, y=-1.5, z=1)),
                  coloraxis_colorbar=dict(title='Voltage'),
                  updatemenus=[dict(type="buttons",
                                    showactive=False,
                                    buttons=[dict(label="Play",
                                                  method="animate",
                                                  args=[None, {"frame": {"duration": 50, "redraw": True}, "fromcurrent": True, "transition": {"duration": 0}}]),
                                             dict(label="Pause",
                                                  method="animate",
                                                  args=[[None], {"frame": {"duration": 0, "redraw": False}, "mode": "immediate", "transition": {"duration": 0}}])])])

# Show the animated 3D plot
fig.show()
