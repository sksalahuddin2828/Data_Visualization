import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the variables
R_vol = 1e6  # 1.00 MΩ
V_scale = 30.0  # 30.0 V
I_galv = sp.Symbol('I_galv')  # Current in the galvanometer (sensitivity)

# Define the equation for sensitivity
sensitivity_eq = sp.Eq(V_scale, I_galv * R_vol)

# Solve for sensitivity
sensitivity_solution = sp.solve(sensitivity_eq, I_galv)

# Create a meshgrid for resistance and voltage
resistance_range = np.linspace(1e5, 1e7, 100)  # Range of resistance values (10^5 to 10^7 Ω)
voltage_range = np.linspace(10, 50, 100)  # Range of voltage values (10 to 50 V)
R, V = np.meshgrid(resistance_range, voltage_range)

# Convert the sensitivity equation to a numpy function
sensitivity_func = sp.lambdify(I_galv, sensitivity_solution[0], 'numpy')

# Calculate sensitivity for each combination of resistance and voltage
sensitivity = sensitivity_func(0.0)  # Pass 0.0 as a placeholder for I_galv

# Calculate sensitivity for the entire array
sensitivity = sensitivity * np.ones_like(R)

# Create a 3D surface plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(np.log10(R), V, sensitivity, cmap='viridis')

# Customize the plot
ax.set_xlabel('Log(R) (Ω)')
ax.set_ylabel('Voltage (V)')
ax.set_zlabel('Sensitivity (A/V)')
ax.set_title('Galvanometer Sensitivity vs. Resistance and Voltage')
ax.view_init(elev=20, azim=-30)

# Show the plot
plt.show()
