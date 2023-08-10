import numpy as np
import plotly.graph_objects as go
import sympy as sp

# Define symbols for symbolic calculations
x, t, A, omega, mu, v = sp.symbols('x t A omega mu v')

# Kinetic Energy Calculation
# Define the kinetic energy equation
kinetic_energy = 0.5 * mu * A**2 * omega**2 * v**2 * sp.cos(2 * sp.pi * v * t - 2 * sp.pi * v * x)

# Convert symbolic expression to a numerical function
kinetic_energy_func = sp.lambdify((A, omega, mu, v, t, x), kinetic_energy, modules=['numpy'])

# Visualize kinetic energy over a wavelength
x_values = np.linspace(0, 1, 100)
kinetic_energy_values = kinetic_energy_func(1, 1, 1, 1, 0, x_values)

kinetic_energy_fig = go.Figure(go.Scatter(x=x_values, y=kinetic_energy_values, mode='lines'))
kinetic_energy_fig.update_layout(
    title='Kinetic Energy Distribution',
    xaxis_title='Position (x)',
    yaxis_title='Kinetic Energy',
)
kinetic_energy_fig.show()

# Potential Energy Calculation
# Define the potential energy equation
potential_energy = 0.5 * mu * omega**2 * A**2 * x**2 * sp.sin(2 * sp.pi * v * t - 2 * sp.pi * v * x)

# Convert symbolic expression to a numerical function
potential_energy_func = sp.lambdify((A, omega, mu, v, t, x), potential_energy, modules=['numpy'])

# Visualize potential energy over a wavelength
potential_energy_values = potential_energy_func(1, 1, 1, 1, 0, x_values)

potential_energy_fig = go.Figure(go.Scatter(x=x_values, y=potential_energy_values, mode='lines'))
potential_energy_fig.update_layout(
    title='Potential Energy Distribution',
    xaxis_title='Position (x)',
    yaxis_title='Potential Energy',
)
potential_energy_fig.show()

# Total Energy and Power Calculation
# Total energy associated with a wavelength
total_energy = kinetic_energy + potential_energy

# Convert symbolic expression to a numerical function for total energy
total_energy_func = sp.lambdify((A, omega, mu, v, t, x), total_energy, modules=['numpy'])

# Convert symbolic expression to a numerical function for time-averaged power
time_averaged_power_func = sp.lambdify((A, omega, mu, v, t, x), time_averaged_power, modules=['numpy'])

# Visualize time-averaged power over a wavelength
power_values = time_averaged_power_func(1, 1, 1, 1, 0, x_values)

power_fig = go.Figure(go.Scatter(x=x_values, y=power_values, mode='lines'))
power_fig.update_layout(
    title='Time-Averaged Power Distribution',
    xaxis_title='Position (x)',
    yaxis_title='Time-Averaged Power',
)
power_fig.show()
