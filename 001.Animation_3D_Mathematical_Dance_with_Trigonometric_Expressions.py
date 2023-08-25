import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Generate data
num_points = 50
currents = np.linspace(0, 5, num_points)
voltages = np.linspace(0, 120, num_points)
currents_mesh, voltages_mesh = np.meshgrid(currents, voltages)
powers = (1/2) * currents_mesh * voltages_mesh

data = pd.DataFrame({
    'Current': currents_mesh.flatten(),
    'Voltage': voltages_mesh.flatten(),
    'Power': powers.flatten()
})

# Create a 3D surface plot for average power
surface_plot = go.Figure(data=[go.Surface(z=powers, x=currents, y=voltages)])
surface_plot.update_layout(
    title='Average Power 3D Surface Visualization',
    scene=dict(
        xaxis_title='Current',
        yaxis_title='Voltage',
        zaxis_title='Power',
    )
)

# Create an animated scatter plot for RMS current and voltage
fig = make_subplots(rows=1, cols=2, specs=[[{'type': 'scatter'}, {'type': 'scatter'}]])
current_values = np.linspace(0, 5, 100)
voltage_values = np.linspace(0, 120, 100)
current_trace = go.Scatter(x=current_values, y=np.sqrt(2) * current_values, mode='lines', name='RMS Current')
voltage_trace = go.Scatter(x=voltage_values, y=np.sqrt(2) * voltage_values, mode='lines', name='RMS Voltage')
fig.add_trace(current_trace, row=1, col=1)
fig.add_trace(voltage_trace, row=1, col=2)
fig.update_layout(title='RMS Current and Voltage Visualization')

# Create an animation for the mathematical dance
animation_steps = 50
theta_values = np.linspace(0, 2 * np.pi, animation_steps)
x_values = np.cos(theta_values)
y_values = np.sin(theta_values)

animation_frames = [go.Frame(data=[go.Scatter(x=[0, x], y=[0, y], mode='lines+markers')]) for x, y in zip(x_values, y_values)]
animation_layout = go.Layout(
    title='Mathematical Dance with Trigonometric Expressions',
    xaxis=dict(range=[-1.2, 1.2]),
    yaxis=dict(range=[-1.2, 1.2]),
    updatemenus=[{'type': 'buttons', 'showactive': False, 'buttons': [{'label': 'Play', 'method': 'animate', 'args': [None, {'frame': {'duration': 100, 'redraw': True}, 'fromcurrent': True}]}]}]
)

animation_plot = go.Figure(data=[go.Scatter(x=[0], y=[0], mode='lines+markers')], layout=animation_layout, frames=animation_frames)

# Display the plots
surface_plot.show()
fig.show()
animation_plot.show()
