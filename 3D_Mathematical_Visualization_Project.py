import numpy as np
import sympy as sp
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from scipy.optimize import fsolve

# Define variables x, y, and z using SymPy symbols
x, y, z = sp.symbols('x y z')

# Given equations
eq1 = x + y + z - 3
eq2 = x*2 + y**2 + z*2 - 4
eq3 = x*3 + y**3 + z*3 - 5

# Numerically solving the equations using fsolve
eq1_func = sp.lambdify((x, y, z), eq1)
eq2_func = sp.lambdify((x, y, z), eq2)
eq3_func = sp.lambdify((x, y, z), eq3)

def equations(variables):
    x, y, z = variables
    return [eq1_func(x, y, z), eq2_func(x, y, z), eq3_func(x, y, z)]

initial_guess = [1, 1, 1]
sol = fsolve(equations, initial_guess)
x_val, y_val, z_val = sol

# Creating a Pandas DataFrame to display the results
data = {'Variable': ['x', 'y', 'z'],
        'Value': [x_val, y_val, z_val]}
df = pd.DataFrame(data)

# 3D Visualization using Plotly
fig = go.Figure()

# Adding initial point as a fixed marker
fig.add_trace(go.Scatter3d(x=[x_val], y=[y_val], z=[z_val], mode='markers',
                           marker=dict(size=8, color='blue')))

# Mathematical dance with more complex expressions and functions
time_values = np.linspace(0, 2*np.pi, 100)

# Define functions for the dance movements
def x_dance(t):
    return np.sin(2*t) + np.cos(3*t) + np.tan(4*t)

def y_dance(t):
    return np.exp(-t) * np.sin(5*t)

def z_dance(t):
    return np.log(1 + np.abs(np.sin(t))) * np.sqrt(t)

# Animate the dance movements
frames = [go.Frame(data=[go.Scatter3d(x=[x_dance(t)], y=[y_dance(t)], z=[z_dance(t)], mode='markers',
                                     marker=dict(size=8, color='red'))],
                   name=str(t)) for t in time_values]

# Adding frames to the figure
for frame in frames:
    fig.add_trace(frame.data[0])

# Define slider properties for the animation
slider_steps = [dict(args=[[f.name], dict(frame=dict(duration=0, redraw=True), fromcurrent=True, mode='immediate')], 
                     label=str(t), method='animate') for f, t in zip(frames, time_values)]
sliders = [dict(active=0, currentvalue={"prefix": "Time: "}, pad={"t": 50}, steps=slider_steps)]

# Set up layout for animation
fig.update_layout(updatemenus=[dict(type='buttons', showactive=False, buttons=[dict(label='Play',
                                    method='animate',
                                    args=[None, dict(frame=dict(duration=50, redraw=True),
                                    fromcurrent=True, mode='immediate')]),
                         dict(label='Pause',
                              method='animate',
                              args=[[None], dict(frame=dict(duration=0, redraw=False), mode='immediate')])])],
                  sliders=sliders, scene=dict(xaxis_title="x", yaxis_title="y", zaxis_title="z"),
                  title="Mathematical Dance", showlegend=False)

# Displaying the results and the visualizations
print("Solutions:")
print(df)
fig.show()
