import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Generate sample data
current_range = np.linspace(0, 10, 50)
resistance_range = np.linspace(1, 5, 50)
current_grid, resistance_grid = np.meshgrid(current_range, resistance_range)
power_grid = current_grid ** 2 * resistance_grid
temperature_rise_grid = power_grid * 0.05

# Create a DataFrame for the data
data = pd.DataFrame({
    'Current': current_grid.flatten(),
    'Resistance': resistance_grid.flatten(),
    'Power': power_grid.flatten(),
    'Temperature_Rise': temperature_rise_grid.flatten()
})

# Create an interactive 3D surface plot
fig = go.Figure(data=[go.Surface(z=data['Power'].values.reshape(50, 50),
                                  x=data['Current'].values.reshape(50, 50),
                                  y=data['Resistance'].values.reshape(50, 50),
                                  colorscale='Viridis')])

fig.update_layout(scene=dict(
    xaxis_title='Current (A)',
    yaxis_title='Resistance (Ω)',
    zaxis_title='Power Dissipation (W)'
))

fig.update_traces(showscale=True)

# Show the interactive 3D plot
fig.show()
