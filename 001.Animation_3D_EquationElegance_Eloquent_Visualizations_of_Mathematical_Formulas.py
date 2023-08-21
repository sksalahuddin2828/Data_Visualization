import numpy as np
import pandas as pd
import sympy as sp
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from scipy.integrate import quad
from mpl_toolkits.mplot3d import Axes3D

# Define the symbols
x, a = sp.symbols('x a')

# Define the integral
integral = sp.integrate(a**2 - x**2, x)

# Calculate the integral
result = integral + 12 * a * sp.ln(sp.Abs(x + a * x - a))

# Display the result
print("Result of the integral:")
sp.pprint(result)

# Create interactive 3D surface plot
x_vals = np.linspace(-5, 5, 100)
a_vals = np.linspace(0.1, 2, 50)
X, A = np.meshgrid(x_vals, a_vals)
Z = X + A * X - A

fig_3d = go.Figure(data=[go.Surface(z=Z, x=X, y=A, colorscale='Viridis')])
fig_3d.update_layout(scene=dict(xaxis_title='x', yaxis_title='a', zaxis_title='Result'),
                     title='3D Visualization of Result')
fig_3d.show()

# Create an animated line plot using Plotly
x_vals = np.linspace(-5, 5, 100)
a_val = 1  # Fix 'a' value for this animation

y_vals = [float(result.evalf(subs={x: val, a: a_val})) for val in x_vals]

df = pd.DataFrame({'x': x_vals, 'y': y_vals})
fig_animated = px.line(df, x='x', y='y', title='Integral Result Animation',
                       labels={'x': 'x', 'y': 'Result'}, template='plotly_dark')

# Add animation
frames = [go.Frame(data=[go.Scatter(x=df['x'][:i], y=df['y'][:i], mode='lines+markers', line=dict(color='orange'))],
                   name=str(i)) for i in range(2, len(df))]

fig_animated.frames = frames

fig_animated.update_layout(updatemenus=[dict(type='buttons',
                                              showactive=False,
                                              buttons=[dict(label='Play',
                                                            method='animate',
                                                            args=[None, dict(frame=dict(duration=100, redraw=True), fromcurrent=True)])])])

fig_animated.show()
