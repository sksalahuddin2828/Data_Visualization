import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Create a DataFrame with voltage, current, and power data
voltage_range = np.linspace(0, 240, 100)
current_range = np.linspace(0, 20, 100)
V, I = np.meshgrid(voltage_range, current_range)
P = V * I

data = pd.DataFrame({'Voltage': V.ravel(), 'Current': I.ravel(), 'Power': P.ravel()})

# Create an interactive scatter plot using Plotly
scatter_fig = px.scatter(data, x='Voltage', y='Current', size='Power', color='Power',
                         labels={'Voltage': 'Voltage (V)', 'Current': 'Current (A)', 'Power': 'Power (W)'},
                         title='Microwave Oven Power Consumption')

# Add a slider to control the marker size (power)
scatter_fig.update_layout(sliders=[{
    'currentvalue': {'prefix': 'Power: '},
    'steps': [{'args': [['marker.size'], [i]],
               'label': str(i),
               'method': 'restyle'} for i in range(10, 101, 10)]
}])

# Create a 3D surface plot of power consumption using Plotly
surface_fig = go.Figure(data=[go.Surface(z=P, x=V, y=I)])
surface_fig.update_layout(scene=dict(xaxis_title='Voltage (V)', yaxis_title='Current (A)', zaxis_title='Power (W)'),
                          title='3D Power Consumption Surface')

# Show the interactive scatter plot
scatter_fig.show()

# Show the interactive 3D surface plot
surface_fig.show()
