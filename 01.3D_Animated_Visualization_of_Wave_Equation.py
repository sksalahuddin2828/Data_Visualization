import numpy as np
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

# Generate data for animated visualization
x_vals = np.linspace(0, 10, 100)
t_vals = np.linspace(0, 5, 50)
X, T = np.meshgrid(x_vals, t_vals)
Y = 0.50 * np.cos(0.20 * np.pi * (-1) * X - 4.00 * np.pi * (-1) * T + np.pi / 10)

# Create an animated 3D surface plot
frames = [go.Frame(data=[go.Surface(z=Y[:i], x=x_vals, y=t_vals[:i], colorscale='viridis')],
                   name=str(i))
          for i in range(1, Y.shape[0])]

fig = go.Figure(data=[go.Surface(z=Y, x=x_vals, y=t_vals, colorscale='viridis')],
                frames=frames)

# Update layout for animated 3D plot
fig.update_layout(scene=dict(zaxis=dict(ticksuffix=' m')))
fig.update_layout(title='Animated Visualization of Wave Equation')
fig.update_layout(updatemenus=[dict(type='buttons', showactive=False, buttons=[dict(label='Play',
                                            method='animate',
                                            args=[None, dict(frame=dict(duration=100, redraw=True), fromcurrent=True, transition=dict(duration=0))])])])

# Display the result and the animated visualization
print(f"The given wave equation {result_message} the linear wave equation.")
fig.show()
