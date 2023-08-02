import numpy as np
import plotly.graph_objects as go
import sympy as sp

r = sp.symbols('r')
recurrence_relation = r**2 - 3*r + 2

roots = sp.solve(recurrence_relation, r)
print("Roots of the equation:", roots)

# Create meshgrid for 3D visualization
r_values = np.linspace(-5, 5, 100)
r, R = np.meshgrid(r_values, r_values)

# Evaluate the solution at each point
Z = R**2 - 3*R + 2

# Create 3D surface plot using Plotly
fig = go.Figure(data=[go.Surface(z=Z, x=r_values, y=r_values)])

# Customize the plot layout
fig.update_layout(scene=dict(
    xaxis_title='r',
    yaxis_title='R',
    zaxis_title='Value'
), title='3D Visualization of the Solution using Plotly')

# Show the interactive 3D plot
fig.show()
