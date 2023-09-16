import numpy as np
import pandas as pd
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import plotly.express as px
from scipy.optimize import minimize

v = 10  # initial velocity (m/s)
theta = np.radians(60)  # angle in radians
x = 4  # vertical component (m)
g = 9.8  # acceleration due to gravity (m/s^2)

horizontal_component = x / (np.tan(theta) - (g * x**2) / (2 * v**2 * np.cos(theta)**2))

t = np.linspace(0, (2 * v * np.sin(theta)) / g, num=100)  # Time array
x_values = horizontal_component * np.cos(theta) * t
y_values = horizontal_component * np.sin(theta) * t - 0.5 * g * t**2

fig = px.line_3d(x=x_values, y=y_values, z=t, labels={'x': 'Horizontal Distance (m)', 'y': 'Vertical Distance (m)', 'z': 'Time (s)'})
fig.update_layout(scene=dict(aspectmode='cube'))
fig.show()

t_sym = sp.Symbol('t')
x_sym = horizontal_component * sp.cos(theta) * t_sym
y_sym = horizontal_component * sp.sin(theta) * t_sym - 0.5 * g * t_sym**2

sp.init_printing(use_unicode=True)
display(x_sym, y_sym)

objective_function = lambda x: -(x[0] / (np.tan(theta) - (g * x[0]**2) / (2 * v**2 * np.cos(theta)**2)))
result = minimize(objective_function, [horizontal_component], bounds=[(0, None)])

max_range = -result.fun
