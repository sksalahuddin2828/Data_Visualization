import numpy as np
import matplotlib.pyplot as plt
from sympy import Symbol, Eq, solve
import math

# Define the given values
emf = 10.0  # EMF of the battery in volts
load_resistance = 0.500  # Load resistance in ohms

# Calculate current using Ohm's Law (V = IR)
I = emf / load_resistance

# Calculate power dissipated using P = I^2 * R
P_load = I**2 * load_resistance

# Visualization
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

# Create a surface plot for power dissipation as a function of EMF and load resistance
emf_values = np.linspace(1.0, 15.0, 100)
load_resistance_values = np.linspace(0.1, 1.0, 100)
EMF, Load_Resistance = np.meshgrid(emf_values, load_resistance_values)
Power = (EMF / Load_Resistance)**2 * Load_Resistance

ax.plot_surface(EMF, Load_Resistance, Power, cmap='viridis')

ax.set_xlabel('EMF (Volts)')
ax.set_ylabel('Load Resistance (Ohms)')
ax.set_zlabel('Power (Watts)')
ax.set_title('Power Dissipation in Battery Circuit')

plt.show()

# Mathematical expression and equation solving using SymPy
V, I, R = Symbol('V'), Symbol('I'), Symbol('R')
equation = Eq(V, I * R)
current_equation = equation.subs({V: emf, R: load_resistance})
current_solution = solve(current_equation, I)[0]

print(f'Current (I) = {current_solution:.2f} A')
print(f'Power Dissipation (P) = {P_load:.2f} W')
