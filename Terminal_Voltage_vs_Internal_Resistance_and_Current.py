import numpy as np
import sympy as sp

# Given data
delta_V = 2.00  # Change in terminal voltage (in volts)
delta_I = 5.00  # Change in current supplied (in amperes)

# Define variables
R_internal = sp.Symbol('R_internal')  # Internal resistance (in ohms)
I = sp.Symbol('I')  # Current supplied (in amperes)
V_emf = sp.Symbol('V_emf')  # Electromotive force (in volts)

# Ohm's Law: V = E - I * R, where V is terminal voltage, E is emf, and R is internal resistance
equation = sp.Eq(delta_V, V_emf - (I + delta_I) * (R_internal))

# Solve for internal resistance
internal_resistance_solution = sp.solve(equation, R_internal)

# Check if emf can be found
if internal_resistance_solution:
    emf_value = sp.solve(sp.Eq(delta_V, V_emf - I * internal_resistance_solution[0]), V_emf)
    if emf_value:
        emf = emf_value[0]
        print(f"Internal Resistance: {internal_resistance_solution[0]} ohms")
        print(f"Electromotive Force (emf): {emf} volts")
    else:
        print("Emf cannot be determined with the given information.")
else:
    print("Internal resistance solution not found.")

# Create a 3D visualization (example: a 3D plot)
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define a range of internal resistance and current values for visualization
R_internal_values = np.linspace(0, 10, 100)
I_values = np.linspace(0, 10, 100)

# Create a meshgrid for 3D plot
R_internal_mesh, I_mesh = np.meshgrid(R_internal_values, I_values)
delta_V_mesh = emf - (I_mesh + delta_I) * R_internal_mesh  # Terminal voltage

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(R_internal_mesh, I_mesh, delta_V_mesh, cmap='viridis')
ax.set_xlabel('Internal Resistance (ohms)')
ax.set_ylabel('Current (A)')
ax.set_zlabel('Terminal Voltage (V)')
ax.set_title('Terminal Voltage vs Internal Resistance and Current')

# Show the plot
plt.show()
