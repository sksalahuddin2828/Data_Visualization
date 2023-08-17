import sympy as sp

x = sp.symbols('x')
f = sp.Function('f')(x)
g = sp.Function('g')(x)

expr = f * g
derivative_expr = sp.diff(expr, x)

# Printing the result
print("Expression:", expr)
print("Derivative:", derivative_expr)

import pandas as pd

data = {'x': [1, 2, 3, 4, 5],
        'f_x': [2, 3, 5, 7, 11],
        'g_x': [1, 4, 9, 16, 25]}

df = pd.DataFrame(data)

# Performing operations
df['f_times_g'] = df['f_x'] * df['g_x']

# Printing the DataFrame
print(df)

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create data
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z)

# Customize the plot
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Parabolic Surface')

# Show the plot
plt.show()

import numpy as np
import plotly.graph_objects as go

# Create data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a scatter plot
fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Sin Curve'))

# Customize the plot
fig.update_layout(title='Dynamic Sin Curve',
                  xaxis_title='X',
                  yaxis_title='Y')

# Show the plot
fig.show()
