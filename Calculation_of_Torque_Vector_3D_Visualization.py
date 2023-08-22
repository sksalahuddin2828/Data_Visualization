import numpy as np
import plotly.graph_objects as go
import pandas as pd
from sympy import symbols, Eq, solve, sin
from IPython.display import display, Markdown
from matplotlib import animation
import matplotlib.pyplot as plt

# Given values
angle_deg = 80
r_perp = 98.5  # meters
force_magnitude = 5.0e5  # Newtons

# Calculate torque magnitude
torque_magnitude = -r_perp * force_magnitude

# Convert angle to radians
angle_rad = np.radians(angle_deg)

# Calculate torque vector components
torque_vector = np.array([
    torque_magnitude * np.sin(angle_rad),
    0,
    torque_magnitude * np.cos(angle_rad)
])

# Create an interactive 3D scatter plot using Plotly
fig = go.Figure(data=[go.Scatter3d(
    x=[0, torque_vector[0]],
    y=[0, torque_vector[1]],
    z=[0, torque_vector[2]],
    mode='markers+lines',
    marker=dict(size=[5, 0], color='blue'),
    line=dict(color='blue', width=5)
)])
fig.update_layout(
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z',
        aspectmode='cube',
        camera=dict(eye=dict(x=1, y=1, z=1))
    )
)

# Display the 3D plot
display(Markdown("### Torque Vector 3D Visualization"))
fig.show()

# Create a Pandas DataFrame for torque components
torque_df = pd.DataFrame({'Component': ['X', 'Y', 'Z'], 'Value': torque_vector})

# Display the DataFrame with torque components
display(Markdown("### Torque Vector Components"))
display(torque_df)

# Define symbols for mathematical expressions
theta = symbols('theta')
torque_expr = -r_perp * force_magnitude * sin(theta)

# Display the torque expression using LaTeX
display(Markdown("### Torque Expression"))
display(Markdown(f"The torque expression is given by: $\\tau = -r_\\perp F \\sin(\\theta)$"))

# Solve for equilibrium angle using SymPy
equilibrium_eq = Eq(torque_expr, 0)
equilibrium_angle = solve(equilibrium_eq, theta)[0]

# Display the equilibrium angle
display(Markdown("### Equilibrium Angle"))

if equilibrium_angle == 0:
    display(Markdown(f"The equilibrium angle $\\theta$ is exactly {equilibrium_angle}."))
else:
    equilibrium_angle_deg = np.degrees(equilibrium_angle)
    display(Markdown(f"The equilibrium angle $\\theta$ is approximately {equilibrium_angle_deg:.2f} degrees."))

# Animation of torque vector rotation
def animate(frame):
    ax.clear()
    ax.quiver(0, 0, 0, torque_vector[0], torque_vector[1], torque_vector[2], color='b')
    ax.set_xlim([0, torque_vector[0]])
    ax.set_ylim([0, torque_vector[1]])
    ax.set_zlim([0, torque_vector[2]])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Torque Vector Rotation')

# Create a 3D plot for animation using Matplotlib
fig_animation = plt.figure()
ax = fig_animation.add_subplot(111, projection='3d')
ani = animation.FuncAnimation(fig_animation, animate, frames=180, interval=50)
plt.close(fig_animation)

# Display the animation
display(Markdown("### Torque Vector Rotation Animation"))
display(ani.to_jshtml())
