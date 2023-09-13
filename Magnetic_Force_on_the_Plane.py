import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

# Given parameters
q = 0.500e-6  # Charge in Coulombs
v = 660.0     # Velocity in m/s
B = 8.00e-5   # Magnetic field in T

# Calculate the magnetic force
F = q * v * B

# Create a DataFrame for the calculation
data = {
    'Parameter': ['Charge (q)', 'Velocity (v)', 'Magnetic Field (B)', 'Magnetic Force (F)'],
    'Value': [q, v, B, F]
}
df = pd.DataFrame(data)

# Create an interactive table using pandas
table = df.to_html(classes='table table-bordered table-hover table-sm')

# Create a 3D scatter plot with plotly
fig = go.Figure(data=[go.Scatter3d(x=[0, 0, 0, 0], y=[0, 0, 0, 0], z=[0, 0, 0, F],
                                   mode='markers+text',
                                   text=df['Parameter'],
                                   marker=dict(size=5))])

fig.update_layout(scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Z'),
                  title='Magnetic Force on the Plane',
                  showlegend=False)

# Display the table and 3D plot
from IPython.display import HTML, display
display(HTML(table))
fig.show()
