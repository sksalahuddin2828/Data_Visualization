import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Define a symbolic variable
x = sp.Symbol('x')

# Define the function
def quadratic_function(a, b, c):
    x = np.linspace(-10, 10, 400)
    y = a * x**2 + b * x + c
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Quadratic Function: ax^2 + bx + c')
    return x, y

# Create interactive widget
a_default = 1.0
b_default = 0.0
c_default = 0.0
x, y = quadratic_function(a_default, b_default, c_default)  # Initialize x and y
interact(quadratic_function, a=(-2, 2, 0.1), b=(-5, 5, 0.1), c=(-10, 10, 0.1))

# Create a Pandas DataFrame
data = {'x': x, 'y': y}
df = pd.DataFrame(data)

# Create an interactive scatter plot using Plotly
fig = px.scatter(df, x='x', y='y', title='Interactive Scatter Plot with Plotly')
fig.show()  # Display the scatter plot interactively

# Create a 3D scatter plot using Plotly
num_points = 100
x_3d = np.random.rand(num_points)
y_3d = np.random.rand(num_points)
z_3d = np.random.rand(num_points)
df_3d = pd.DataFrame({'x': x_3d, 'y': y_3d, 'z': z_3d})
fig_3d = px.scatter_3d(df_3d, x='x', y='y', z='z', title='Interactive 3D Scatter Plot with Plotly')
fig_3d.show()  # Display the 3D scatter plot interactively

# Create matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
C = np.dot(A, B)

print("Matrix A:")
print(A)
print("Matrix B:")
print(B)
print("Matrix C (Result of A * B):")
print(C)

# Create an animated sine wave using Plotly
t = np.linspace(0, 10, 100)
x = t
y = np.sin(x)
fig_animation = go.FigureWidget(data=go.Scatter(x=x, y=y, mode='lines'))

def animate_sine_wave(interval):
    with fig_animation.batch_update():
        x = t + interval
        y = np.sin(x)
        fig_animation.data[0].x = x
        fig_animation.data[0].y = y

interval_slider = interact(animate_sine_wave, interval=(0, 10, 0.1))
display(fig_animation)
