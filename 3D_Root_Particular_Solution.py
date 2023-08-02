import numpy as np
import plotly.graph_objects as go

def particular_solution(r, R, C1, C2, root1, root2):
    return C1 * root1**r + C2 * root2**r

# Roots of the characteristic equation
root1 = 1
root2 = 2

# Initial conditions
a0 = 0
a1 = 1

# Solve for C1 and C2 using initial conditions
C2 = (a0 - root1*a1) / (root2 - root1)
C1 = a1 - C2

# Create meshgrid for 3D visualization
r_values = np.linspace(-5, 5, 100)
R_values = np.linspace(-5, 5, 100)
r, R = np.meshgrid(r_values, R_values)

# Evaluate the particular solution at each point
Z = particular_solution(r, R, C1, C2, root1, root2)

# Create 3D surface plot using Plotly
fig = go.Figure(data=[go.Surface(z=Z, x=r_values, y=R_values)])

# Customize the plot layout
fig.update_layout(scene=dict(
    xaxis_title='r',
    yaxis_title='R',
    zaxis_title='Value'
), title='3D Visualization of the Particular Solution using Plotly')

# Show the interactive 3D plot
fig.show()
