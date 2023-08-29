import numpy as np
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# Given values
voltage = 120  # Volts
current = 0.01  # Amperes (10 mA)
voltage_across_person = 0  # Since the person doesn't feel it

# Calculate minimum resistance
resistance = voltage / current

# Create a range of resistance values for visualization
resistance_range = np.linspace(0.01, 1000, 100)
voltage_range = resistance_range * current

# Create a Pandas DataFrame
data = pd.DataFrame({'Resistance': resistance_range, 'Voltage': voltage_range})

# Create an interactive scatter plot using Plotly Express
scatter_plot = px.scatter(data, x='Resistance', y='Voltage', title='Voltage vs. Resistance',
                          labels={'Resistance': 'Resistance (Ohms)', 'Voltage': 'Voltage (Volts)'})

# Highlight the minimum resistance point
scatter_plot.add_trace(go.Scatter(x=[resistance], y=[voltage_across_person],
                                  mode='markers', name='Minimum Resistance',
                                  marker=dict(size=10, color='red', symbol='star')))

# Create an interactive 3D scatter plot using Plotly Express
fig = make_subplots(rows=1, cols=1, specs=[[{'type': 'scatter3d'}]])
scatter3d_plot = px.scatter_3d(data, x='Resistance', y='Voltage', z=np.zeros_like(resistance_range),
                               title='Minimum Resistance Calculation',
                               labels={'Resistance': 'Resistance (Ohms)', 'Voltage': 'Voltage (Volts)'})

# Highlight the minimum resistance point in the 3D plot
scatter3d_plot.add_trace(go.Scatter3d(x=[resistance], y=[voltage_across_person], z=[0],
                                      mode='markers', name='Minimum Resistance',
                                      marker=dict(size=10, color='red', symbol='circle')))

# Show the interactive plots
scatter_plot.show()
scatter3d_plot.show()
