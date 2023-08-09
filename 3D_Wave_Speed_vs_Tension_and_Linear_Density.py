import numpy as np
import plotly.graph_objs as go
import sympy as sp

# Step 1: Deriving the Wave Speed Equation
v, FT, mu = sp.symbols('v FT mu')
wave_speed_equation = sp.sqrt(FT / mu)

# Step 2: Calculating Wave Speed
tension_values = np.linspace(1, 200, 100)
linear_density_values = np.linspace(0.01, 0.2, 100)

tension_mesh, linear_density_mesh = np.meshgrid(tension_values, linear_density_values)
wave_speed_values = np.sqrt(tension_mesh / linear_density_mesh)

# Create a 3D surface plot using Plotly
surface = go.Surface(
    x=tension_mesh, y=linear_density_mesh, z=wave_speed_values,
    colorscale='Viridis', colorbar_title='Wave Speed'
)

layout = go.Layout(title='Wave Speed vs Tension and Linear Density',
                   scene=dict(
                       xaxis_title='Tension (FT)',
                       yaxis_title='Linear Density (mu)',
                       zaxis_title='Wave Speed (v)'
                   ))

# Adding the 3D surface plot
fig = go.Figure(data=[surface], layout=layout)
fig.update_layout(scene_aspectmode='data')
fig.update_layout(scene_zaxis_type='log')  # Adjust the z-axis to log scale

# Additional Mathematical Expression
expression = sp.latex(wave_speed_equation)
print("LaTeX Expression for Wave Speed:", expression)

fig.show()
