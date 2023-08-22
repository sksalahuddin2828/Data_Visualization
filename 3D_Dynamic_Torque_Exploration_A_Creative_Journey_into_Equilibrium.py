import numpy as np
import plotly.graph_objects as go
import pandas as pd
from sympy import symbols, Eq, solve, sin
from IPython.display import display, Markdown, HTML
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

# Create an interactive 3D scatter plot using Plotly for initial torque vector visualization
initial_torque_fig = go.Figure(data=[go.Scatter3d(
    x=[0, torque_vector[0]],
    y=[0, torque_vector[1]],
    z=[0, torque_vector[2]],
    mode='markers+lines',
    marker=dict(size=[5, 0], color='blue'),
    line=dict(color='blue', width=5)
)])
initial_torque_fig.update_layout(
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z',
        aspectmode='cube',
        camera=dict(eye=dict(x=1, y=1, z=1))
    )
)

# Display the initial torque vector 3D visualization
display(Markdown("### Initial Torque Vector 3D Visualization"))
initial_torque_fig.show()

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

# Animate the rotation of the torque vector
def animate_rotation(frame):
    ax.clear()
    angle_rad = np.radians(frame)
    rotated_torque_vector = np.array([
        torque_magnitude * np.sin(angle_rad),
        0,
        torque_magnitude * np.cos(angle_rad)
    ])
    ax.quiver(0, 0, 0, rotated_torque_vector[0], rotated_torque_vector[1], rotated_torque_vector[2], color='b')
    ax.set_xlim([-torque_magnitude, torque_magnitude])
    ax.set_ylim([-torque_magnitude, torque_magnitude])
    ax.set_zlim([-torque_magnitude, torque_magnitude])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Torque Vector Rotation')

# Create a 3D plot for animation using Matplotlib
rotation_animation_fig = plt.figure()
ax = rotation_animation_fig.add_subplot(111, projection='3d')
rotation_ani = animation.FuncAnimation(rotation_animation_fig, animate_rotation, frames=180, interval=50)
plt.close(rotation_animation_fig)

# Display the torque vector rotation animation
display(Markdown("### Torque Vector Rotation Animation"))
display(rotation_ani.to_jshtml())

# Additional explanations, visualizations, and creative elements
display(Markdown("### Exploring Torque Equilibrium"))

# Create a range of angles for exploration
exploration_angles = np.linspace(0, 360, 100)
torque_magnitudes = -r_perp * force_magnitude * np.sin(np.radians(exploration_angles))

# Create a line chart to visualize torque magnitudes over different angles
exploration_fig = go.Figure(data=[go.Scatter(
    x=exploration_angles,
    y=torque_magnitudes,
    mode='lines',
    marker=dict(color='red'),
    line=dict(width=2)
)])
exploration_fig.update_layout(
    xaxis_title='Angle (degrees)',
    yaxis_title='Torque Magnitude (N⋅m)',
    title='Exploring Torque Equilibrium',
    showlegend=False
)

# Display the exploration line chart
display(Markdown("### Exploring Torque Equilibrium"))
exploration_fig.show()
display(Markdown("### Conclusion"))
display(Markdown("In this creative project, we explored the concept of torque and its equilibrium in a dynamic and interactive manner. We started by visualizing the initial torque vector and its components. We then derived the torque expression and solved for the equilibrium angle symbolically. The equilibrium angle indicates the angle at which the torque is in balance, and any further rotation would require additional torque to counteract the clockwise torque applied."))
display(Markdown("The rotation animation provided an insightful visual representation of how the torque vector changes as the angle varies. We also explored how torque magnitude changes across different angles, showcasing the importance of the equilibrium angle."))
display(Markdown("This project not only enhanced our understanding of torque and equilibrium but also showcased the creative potential of combining mathematics, physics, programming, and visualization techniques."))
