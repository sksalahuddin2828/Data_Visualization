import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Define symbols for symbolic calculations
x, t, A, omega, mu, v = sp.symbols('x t A omega mu v')

# Kinetic Energy Calculation
# Define the kinetic energy equation
kinetic_energy = 0.5 * mu * A**2 * omega**2 * v**2 * sp.cos(2 * sp.pi * v * t - 2 * sp.pi * v * x)

# Visualize kinetic energy over a wavelength
x_values = np.linspace(0, 1, 100)
kinetic_energy_values = [kinetic_energy.subs([(A, 1), (omega, 1), (mu, 1), (v, 1), (t, 0), (x, val)]) for val in x_values]

plt.plot(x_values, kinetic_energy_values)
plt.xlabel('Position (x)')
plt.ylabel('Kinetic Energy')
plt.title('Kinetic Energy Distribution')
plt.show()

# Potential Energy Calculation
# Define the potential energy equation
potential_energy = 0.5 * mu * omega**2 * A**2 * x**2 * sp.sin(2 * sp.pi * v * t - 2 * sp.pi * v * x)

# Visualize potential energy over a wavelength
potential_energy_values = [potential_energy.subs([(A, 1), (omega, 1), (mu, 1), (v, 1), (t, 0), (x, val)]) for val in x_values]

plt.plot(x_values, potential_energy_values)
plt.xlabel('Position (x)')
plt.ylabel('Potential Energy')
plt.title('Potential Energy Distribution')
plt.show()

# Total Energy and Power Calculation
# Total energy associated with a wavelength
total_energy = kinetic_energy + potential_energy

# Time-averaged power calculation
time_averaged_power = total_energy / (2 * sp.pi / omega)

# Visualize time-averaged power over a wavelength
power_values = [time_averaged_power.subs([(A, 1), (omega, 1), (mu, 1), (v, 1), (t, 0), (x, val)]) for val in x_values]

plt.plot(x_values, power_values)
plt.xlabel('Position (x)')
plt.ylabel('Time-Averaged Power')
plt.title('Time-Averaged Power Distribution')
plt.show()
