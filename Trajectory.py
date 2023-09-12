# Import necessary libraries
import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sympy as sp
from scipy.integrate import odeint
import ipywidgets as widgets
from IPython.display import display
from matplotlib.animation import FuncAnimation

# Constants
charge = 1.6e-19  # Charge in Coulombs
mass = 9.10938356e-31  # Mass of an electron (kg)
magnetic_field = np.array([0, 0, 1])  # Magnetic field vector (T)

# Define the Lorentz force equation as a system of differential equations
def lorentz_equations(state, t):
    x, y, z, vx, vy, vz = state
    dxdt = vx
    dydt = vy
    dzdt = vz
    dvxdt = (charge / mass) * (vy * magnetic_field[2] - vz * magnetic_field[1])
    dvydt = (charge / mass) * (vz * magnetic_field[0] - vx * magnetic_field[2])
    dvzdt = (charge / mass) * (vx * magnetic_field[1] - vy * magnetic_field[0])
    return [dxdt, dydt, dzdt, dvxdt, dvydt, dvzdt]

# Create time points for simulation
time = np.linspace(0, 10, 1000)

# Create a function to simulate particle motion
def simulate_particle_motion(charge, initial_velocity):
    initial_state = [0, 0, 0, initial_velocity[0], initial_velocity[1], initial_velocity[2]]
    particle_trajectory = odeint(lorentz_equations, initial_state, time)
    return particle_trajectory

# Create an interactive widget for user input
charge_widget = widgets.FloatSlider(value=1.6e-19, min=1e-19, max=1e-18, step=1e-19, description='Charge (C)')
initial_velocity_widget = widgets.FloatSlider(value=1, min=0, max=10, step=0.1, description='Initial Velocity (m/s)')

# Create a function to update and visualize the particle motion
def update_particle_motion(charge, initial_velocity):
    particle_trajectory = simulate_particle_motion(charge, [initial_velocity, 0, 0])

    # Create a 3D plot of particle trajectories
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(particle_trajectory[:, 0], particle_trajectory[:, 1], particle_trajectory[:, 2], label='Trajectory')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.legend()
    plt.show()

# Display the interactive widget
widgets.interactive(update_particle_motion, charge=charge_widget, initial_velocity=initial_velocity_widget)
