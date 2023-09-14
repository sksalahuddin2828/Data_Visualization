import numpy as np

# Define the parameters for the charged particle
charge = 1.6e-19  # Charge of the particle in coulombs (e.g., electron charge)
mass = 9.11e-31  # Mass of the particle in kilograms (e.g., electron mass)
initial_position = np.array([0.0, 0.0, 0.0])  # Initial position [x, y, z] in meters
velocity = np.array([1.0, 0.0, 0.0])  # Initial velocity [vx, vy, vz] in meters per second
magnetic_field = np.array([0.0, 0.0, 1.0])  # Magnetic field [Bx, By, Bz] in tesla

# Simulation parameters
time_step = 1e-10  # Time step for the simulation in seconds
num_steps = 1000  # Number of time steps for the simulation

def calculate_trajectory(charge, mass, velocity, magnetic_field, initial_position, time_step, num_steps):
    # Initialize arrays to store position and velocity at each time step
    positions = np.zeros((num_steps, 3))
    velocities = np.zeros((num_steps, 3))

    # Initial conditions
    positions[0] = initial_position
    velocities[0] = velocity

    for i in range(1, num_steps):
        # Calculate the Lorentz force (magnetic force) on the charged particle
        magnetic_force = charge * np.cross(velocities[i - 1], magnetic_field)
        
        # Calculate acceleration using F = ma
        acceleration = magnetic_force / mass
        
        # Update velocity and position using the Runge-Kutta method
        k1v = acceleration * time_step
        k1x = velocities[i - 1] * time_step
        
        k2v = acceleration * time_step
        k2x = (velocities[i - 1] + k1v / 2) * time_step
        
        velocities[i] = velocities[i - 1] + k2v
        positions[i] = positions[i - 1] + k2x

    return positions

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Simulate the particle trajectory
positions = calculate_trajectory(charge, mass, velocity, magnetic_field, initial_position, time_step, num_steps)

# Create a 3D plot of the trajectory
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(positions[:, 0], positions[:, 1], positions[:, 2])

# Customize the plot (labels, title, etc.)

plt.show()
