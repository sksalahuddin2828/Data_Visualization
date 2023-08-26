import numpy as np
import plotly.graph_objects as go

# Create a meshgrid for resistance and current
R_vals = np.linspace(1, 20, 100)
Irms_vals = np.linspace(1, 15, 100)
R, Irms = np.meshgrid(R_vals, Irms_vals)

# Calculate average power using Irms^2 * R formula
Pave_surface = (Irms**2) * R

# Create a 3D surface plot
fig = go.Figure(data=[go.Surface(z=Pave_surface, x=R, y=Irms)])

fig.update_layout(title='Power vs. Resistance and Current',
                  scene=dict(xaxis_title='Resistance', yaxis_title='Irms', zaxis_title='Power'))

fig.show()
