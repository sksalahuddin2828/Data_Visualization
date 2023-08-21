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

# Create interactive 3D surface plot with mathematical expression annotation
x_vals = np.linspace(-5, 5, 100)
a_vals = np.linspace(0.1, 2, 50)
X, A = np.meshgrid(x_vals, a_vals)
Z = X + A * X - A

fig_3d = go.Figure(data=[go.Surface(z=Z, x=X, y=A, colorscale='Viridis')])
fig_3d.add_trace(go.Scatter3d(x=[0], y=[1], z=[float(result.evalf(subs={x: 0, a: 1}))],
                              mode='markers+text', text=f'Result: {result}', textposition='bottom center'))
fig_3d.update_layout(scene=dict(xaxis_title='x', yaxis_title='a', zaxis_title='Result'),
                     title='3D Visualization of Result with Expression Annotation')
fig_3d.show()

# Create an animated line plot with additional function
x_vals = np.linspace(-5, 5, 100)
a_val = 1  # Fix 'a' value for this animation

y_vals = [float(result.evalf(subs={x: val, a: a_val})) for val in x_vals]

additional_function = np.sin(x_vals) * 5  # Additional function for creativity

df = pd.DataFrame({'x': x_vals, 'y_result': y_vals, 'y_function': additional_function})
fig_animated = px.line(df, x='x', y=['y_result', 'y_function'],
                       title='Integral Result Animation with Additional Function',
                       labels={'x': 'x', 'value': 'Value'}, template='plotly_dark')

fig_animated.update_traces(mode='lines+markers')
fig_animated.update_layout(legend_title_text='Function',
                          updatemenus=[dict(type='buttons',
                                            showactive=False,
                                            buttons=[dict(label='Play',
                                                          method='animate',
                                                          args=[None, dict(frame=dict(duration=100, redraw=True), fromcurrent=True)])])])

# Add animation
frames = [go.Frame(data=[go.Scatter(x=df['x'][:i], y=df['y_result'][:i], mode='lines+markers', name='Integral Result'),
                         go.Scatter(x=df['x'][:i], y=df['y_function'][:i], mode='lines+markers', name='Additional Function')],
                   name=str(i)) for i in range(2, len(df))]

fig_animated.frames = frames

fig_animated.show()
