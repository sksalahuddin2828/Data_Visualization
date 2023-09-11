import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sympy import symbols, Eq, solve

# Define symbols for resistance, capacitance, and time
R, C, t = symbols('R C t')

# Define the equation τ = RC
equation = Eq(R * C, t)

# Solve the equation for R * C
resistance = 10  # Example resistance value in ohms
capacitance = 5   # Example capacitance value in farads
time_result = solve(equation.subs({R: resistance, C: capacitance}), t)[0]

# Verify that the units are in seconds (s)
units_verification = (resistance, capacitance, time_result)
print(f"Resistance: {resistance} ohms")
print(f"Capacitance: {capacitance} farads")
print(f"Time (τ): {time_result} seconds")
print(f"Units Verification: Resistance * Capacitance = Time: {units_verification} seconds")

# Create a 3D plot to visualize the relationship between R, C, and τ
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Generate a range of resistance and capacitance values
resistance_values = np.linspace(1, 20, 100)
capacitance_values = np.linspace(1, 10, 100)
resistance_values, capacitance_values = np.meshgrid(resistance_values, capacitance_values)
time_values = resistance_values * capacitance_values

# Plot the 3D surface
ax.plot_surface(resistance_values, capacitance_values, time_values, cmap='viridis')

ax.set_xlabel('Resistance (Ω)')
ax.set_ylabel('Capacitance (F)')
ax.set_zlabel('Time (s)')
ax.set_title('Relationship between Resistance, Capacitance, and Time')

plt.show()
