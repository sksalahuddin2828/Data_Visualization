import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Function to calculate parallel resistance
def parallel_resistance(galvanometer_resistance, full_scale_current):
    return galvanometer_resistance / (full_scale_current / 1000) - galvanometer_resistance

# Define symbolic variables for resistance, current, and sensitivity
R, I, S = sp.symbols('R I S')

# Create an equation for parallel resistance
equation = sp.Eq(1 / R, (I / S) - (1 / 10))

# Solve the equation symbolically
solution = sp.solve(equation, R)

# Define current and sensitivity values for plotting
current_values = np.linspace(0.001, 50, 100)  # A
sensitivity_values = np.linspace(0.001, 500, 100)  # μA

# Create a meshgrid for 3D visualization
I, S = np.meshgrid(current_values, sensitivity_values)
R = parallel_resistance(10, I)

# Create 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(I, S, R, cmap='viridis')
ax.set_xlabel('Current (A)')
ax.set_ylabel('Sensitivity (μA)')
ax.set_zlabel('Resistance (Ω)')
plt.title('Parallel Resistance vs. Current and Sensitivity')
plt.show()

# Example calculations
full_scale_current_a = 20  # A
full_scale_current_b = 0.1  # A

resistance_a = parallel_resistance(10, full_scale_current_a)
resistance_b = parallel_resistance(10, full_scale_current_b)

print(f"Required Resistance (a): {resistance_a:.2f} Ω")
print(f"Required Resistance (b): {resistance_b:.2f} Ω")
