import numpy as np
import pandas as pd
import plotly.graph_objects as go
import sympy as sp

# Define symbols
x, t = sp.symbols('x t')
v = sp.symbols('v', positive=True)  # Wave speed

# Define the given wave equation
y = 0.50 * sp.cos(0.20 * sp.pi * (-1) * x - 4.00 * sp.pi * (-1) * t + sp.pi / 10)

# Calculate second partial derivatives
partial2_y_x2 = sp.diff(y, x, x)
partial2_y_t2 = sp.diff(y, t, t)

# Check if the wave equation satisfies the linear wave equation
is_linear_wave = sp.simplify(partial2_y_x2 / (1 / v**2) - partial2_y_t2)

if is_linear_wave == 0:
    result_message = "satisfies"
else:
    result_message = "does not satisfy"

# Generate data for interactive visualization
x_vals = np.linspace(0, 10, 100)
t_vals = np.linspace(0, 5, 50)
X, T = np.meshgrid(x_vals, t_vals)
Y = 0.50 * np.cos(0.20 * np.pi * (-1) * X - 4.00 * np.pi * (-1) * T + np.pi / 10)

# Create DataFrame for interactive visualization
df = pd.DataFrame(data=Y, columns=x_vals, index=t_vals)

# Create Plotly surface plot for the wave equation
fig = go.Figure(data=[
    go.Surface(z=df.values, x=df.columns, y=df.index, colorscale='viridis')
])

# Update z-axis layout with tick suffix
fig.update_layout(scene=dict(zaxis=dict(ticksuffix=' m')))
fig.update_layout(title='Visualization of Wave Equation')

# Display the result and the visualization
print(f"The given wave equation {result_message} the linear wave equation.")
fig.show()
