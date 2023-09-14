import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Constants
charge = 1.6e-19  # Charge of the particle in coulombs (e.g., electron charge)
mass = 9.11e-31  # Mass of the particle in kilograms (e.g., electron mass)
initial_position = np.array([0.0, 0.0, 0.0])  # Initial position [x, y, z] in meters
initial_velocity = np.array([1.0e6, 0.0, 0.0])  # Initial velocity [vx, vy, vz] in m/s
magnetic_field_strength = 1.0  # Strength of the magnetic field in tesla
angle_to_field = np.pi / 4  # Angle of initial velocity with respect to the magnetic field (45 degrees)

# Derived parameters
velocity_magnitude = np.linalg.norm(initial_velocity)
gyro_radius = (mass * velocity_magnitude) / (charge * magnetic_field_strength)
gyro_frequency = (charge * magnetic_field_strength) / mass
period = 2 * np.pi / gyro_frequency

# Simulation parameters
time_step = period / 100  # Time step for the simulation
num_steps = 1000  # Number of time steps for the simulation

# Initialize arrays to store position and velocity at each time step
positions = np.zeros((num_steps, 3))
velocities = np.zeros((num_steps, 3))

# Initial conditions
positions[0] = initial_position
velocities[0] = initial_velocity

for i in range(1, num_steps):
    # Calculate the Lorentz force (magnetic force) on the charged particle
    magnetic_force = charge * np.cross(velocities[i - 1], magnetic_field_strength * np.array([np.cos(angle_to_field), np.sin(angle_to_field), 0]))

    # Calculate acceleration using F = ma
    acceleration = magnetic_force / mass

    # Update velocity and position using the Runge-Kutta method
    k1v = acceleration * time_step
    k1x = velocities[i - 1] * time_step

    k2v = acceleration * time_step
    k2x = (velocities[i - 1] + k1v / 2) * time_step

    velocities[i] = velocities[i - 1] + k2v
    positions[i] = positions[i - 1] + k2x

# Create a Pandas DataFrame for data analysis and presentation
df = pd.DataFrame(positions, columns=['X', 'Y', 'Z'])
df['Time'] = np.linspace(0, num_steps * time_step, num_steps)

# Calculate gyro radius for each time step
df['Gyro Radius'] = gyro_radius

# Create an interactive 3D plot using Plotly
fig = go.Figure(data=[go.Scatter3d(x=df['X'], y=df['Y'], z=df['Z'], mode='lines+markers', marker=dict(size=4),
                                   line=dict(width=2, color=df['Time'], colorscale='Viridis'))])

# Customize the plot (labels, title, etc.)
fig.update_layout(scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Z'),
                  title='Charged Particle Motion in a Magnetic Field')

# Create a 2D plot for the gyro radius over time
fig2 = px.line(df, x='Time', y='Gyro Radius', labels={'Time': 'Time (s)', 'Gyro Radius': 'Gyro Radius (m)'})
fig2.update_layout(title='Gyro Radius vs. Time')

# Show the Plotly plots
fig.show()
fig2.show()
