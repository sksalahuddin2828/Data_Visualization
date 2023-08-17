import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import pandas as pd
import plotly.express as px
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

# Define symbolic variables and functions
x = sp.symbols('x')
u = sp.Function('u')(x)
f_u = u ** 2 + 3 * u + 1

# Calculate the derivative using Sympy
du_dx = sp.diff(f_u, x)

# Print results
print("Original function f(u):", f_u)
print("Derivative of f(u) with respect to x:", du_dx)

# Generate some sample data
x_values = np.linspace(0, 10, 100)
y_values = np.sin(x_values) + np.random.normal(0, 0.1, 100)

# Create a DataFrame using Pandas
df = pd.DataFrame({'x': x_values, 'y': y_values})

# Calculate moving average using Numpy
window_size = 5
df['moving_average'] = np.convolve(df['y'], np.ones(window_size)/window_size, mode='same')

# Create an interactive visualization using Plotly Express
fig_plotly = px.scatter(df, x='x', y='y', title='Sample Data with Moving Average')
fig_plotly.add_scatter(x=df['x'], y=df['moving_average'], mode='lines', name='Moving Average')

# Create an animated visualization using Matplotlib
fig_anim, ax_anim = plt.subplots()
x_anim = np.linspace(0, 2 * np.pi, 100)
line_anim, = ax_anim.plot(x_anim, np.sin(x_anim))

def update(frame):
    line_anim.set_ydata(np.sin(x_anim + frame / 10))
    return line_anim,

ani = FuncAnimation(fig_anim, update, frames=np.arange(0, 20), interval=200)
plt.close(fig_anim)  # Prevents duplicate animation display

# Create a 3D function visualization using Matplotlib
fig_3d = plt.figure()
ax_3d = fig_3d.add_subplot(111, projection='3d')
u_vals = np.linspace(-5, 5, 100)
x_vals = np.linspace(0, 10, 100)
U, X = np.meshgrid(u_vals, x_vals)
Z = U ** 2 + 3 * U + 1
ax_3d.plot_surface(X, U, Z, cmap='viridis')
ax_3d.set_xlabel('x')
ax_3d.set_ylabel('u')
ax_3d.set_zlabel('f(u)')

# Combine all plots into a single visualization
from matplotlib.gridspec import GridSpec

fig_combined = plt.figure(constrained_layout=True, figsize=(10, 8))
gs = GridSpec(3, 2, figure=fig_combined)

ax1 = fig_combined.add_subplot(gs[0, :])
ax2 = fig_combined.add_subplot(gs[1, :])
ax3 = fig_combined.add_subplot(gs[2, 0], projection='3d')  # Use projection='3d'
ax4 = fig_combined.add_subplot(gs[2, 1])

# Adding plots to the grid
ax1.set_title("Original Function and Derivative")
ax1.plot(x_values, y_values, label='Original Data')
ax1.plot(df['x'], df['moving_average'], label='Moving Average')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.legend()

ax2.set_title("Animated Sinusoidal Function")
ax2.set_xlabel('x')
ax2.set_ylabel('sin(x)')
ax2.set_xlim(0, 2 * np.pi)
ax2.set_ylim(-1.5, 1.5)
line_anim, = ax2.plot(x_anim, np.sin(x_anim))

ax3.set_title("3D Function Visualization")
ax3.plot_surface(X, U, Z, cmap='viridis')
ax3.set_xlabel('x')
ax3.set_ylabel('u')
ax3.set_zlabel('f(u)')

# Display Plotly figure directly
ax4.set_title("Interactive Data Visualization")
ax4.axis('off')  # Turn off axes for this subplot

# Display the Plotly figure directly
fig_plotly.update_layout(height=400)
fig_plotly.show()

# Show the combined plot
plt.show()
