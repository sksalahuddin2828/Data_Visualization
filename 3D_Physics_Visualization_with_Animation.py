import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots

# Given data
voltage_cell = 1.58  # Volts
internal_resistance = 0.200  # Ohms
current_load = 8.50  # Amperes

# (a) Calculate terminal voltage
def calculate_terminal_voltage(current, internal_resistance):
    return voltage_cell - current * internal_resistance

# (b) Calculate the load resistance using Ohm's law
def calculate_load_resistance(terminal_voltage, current):
    return terminal_voltage / current

# Create a grid of values for current and load resistance
current_vals = np.linspace(0.01, 10, 100)  # Avoid division by zero
load_resistance_vals = np.linspace(0.01, 10, 100)

# Calculate terminal voltage for the grid
terminal_voltage_vals = calculate_terminal_voltage(current_vals, internal_resistance)

# Calculate load resistance for the grid
load_resistance_grid = np.outer(load_resistance_vals, np.ones(len(current_vals)))
terminal_voltage_grid = np.outer(terminal_voltage_vals, np.ones(len(load_resistance_vals))).T

# Calculate current using Ohm's law for the grid
current_grid = terminal_voltage_grid / load_resistance_grid

# Create Pandas DataFrames to store the data
data = pd.DataFrame({'Current (A)': current_vals,
                     'Load Resistance (Ω)': load_resistance_vals,
                     'Terminal Voltage (V)': terminal_voltage_vals})

# Create an animation
fig = make_subplots(rows=1, cols=2, specs=[[{'type': 'surface'}, {'type': 'scatter3d'}]],
                    subplot_titles=('Terminal Voltage vs. Load Resistance', 'Current vs. Load Resistance'))

# Create a surface plot of terminal voltage vs. load resistance
surface_plot = go.Surface(z=current_grid, x=load_resistance_vals, y=current_vals, colorscale='Viridis')
fig.add_trace(surface_plot, row=1, col=1)

# Create a scatter plot of current vs. load resistance
scatter_plot = go.Scatter3d(x=load_resistance_vals, y=current_vals, z=terminal_voltage_vals,
                            marker=dict(size=3, opacity=0.5),
                            line=dict(color='blue', width=2))
fig.add_trace(scatter_plot, row=1, col=2)

# Add labels and titles
fig.update_layout(scene=dict(xaxis_title='Load Resistance (Ω)',
                             yaxis_title='Current (A)',
                             zaxis_title='Terminal Voltage (V)'),
                  scene2=dict(xaxis_title='Load Resistance (Ω)',
                              yaxis_title='Current (A)',
                              zaxis_title='Terminal Voltage (V)'))
fig.update_layout(title='Physics Visualization with Animation')

# Define animation frames
frames = [go.Frame(data=[go.Surface(z=current_grid[:i + 1, :])],
                   traces=[0], name=f'Frame {i + 1}') for i in range(len(current_vals))]

# Add animation frames
fig.update(frames=frames)

# Show the interactive plot
fig.show()
