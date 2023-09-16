import numpy as np
import sympy as sp
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Given value
sin_theta = 1/3

# Calculate sec θ
cos_theta = sp.sqrt(1 - sin_theta**2)
sec_theta = 1 / cos_theta
sec_theta_val = sec_theta.evalf()

# Additional mathematical calculations and functions
tan_theta = sin_theta / cos_theta
cot_theta = 1 / tan_theta

# Create a DataFrame for visualization
sin_theta_values = np.linspace(0, 1, 100)
cos_theta_values = np.sqrt(1 - sin_theta_values**2)
sec_theta_values = 1 / np.sqrt(1 - sin_theta_values**2)
data = {'sin_theta': sin_theta_values, 'cos_theta': cos_theta_values, 'sec_theta': sec_theta_values}
df = pd.DataFrame(data)

# Create an interactive scatter plot
scatter_plot = px.scatter_3d(df, x='sin_theta', y='cos_theta', z='sec_theta',
                             title="Trigonometric Relationship",
                             labels={'sin_theta': 'sin θ', 'cos_theta': 'cos θ', 'sec_theta': 'sec θ'})

scatter_plot.update_traces(marker=dict(size=5))  # Adjust marker size

# Create an animation of a point moving on the unit circle
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.set_rmax(1)
ax.set_title("Unit Circle Animation")

def animate(i):
    ax.clear()
    ax.set_rmax(1)
    ax.set_title("Unit Circle Animation")
    theta = np.linspace(0, 2 * np.pi, 1000)
    ax.plot(theta, np.ones_like(theta), color='gray')
    ax.plot(theta[:i], np.ones_like(theta[:i]), color='blue')
    ax.plot([theta[i], theta[i]], [0, 1], color='red')

ani = FuncAnimation(fig, animate, frames=100, interval=100)

# Create a dynamic equation
x = sp.symbols('x')
dynamic_eq = sp.Eq(sp.sin(x), sin_theta)
solutions = sp.solve(dynamic_eq, x)

# Presentation
print(f"Given sin θ = {sin_theta}")
print(f"Calculated sec θ = {sec_theta_val:.4f}")

scatter_plot.show()
plt.show()
