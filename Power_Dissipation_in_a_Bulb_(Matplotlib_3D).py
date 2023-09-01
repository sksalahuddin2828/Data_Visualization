import numpy as np
import sympy as sp
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import plotly.express as px

# Given values
voltage_source = 120  # V
wire_resistance = 0.400  # Ω
bulb_power_nominal = 75.0  # W
current_total = 15.0  # A

# Create a symbolic variable for current through the bulb
current_bulb = sp.symbols('I_bulb')

# Calculate the bulb resistance using Ohm's Law
bulb_resistance = voltage_source / current_bulb

# Calculate the power dissipated by the bulb
bulb_power = current_bulb**2 * bulb_resistance

# Solve for current through the bulb
eq = sp.Eq(current_total, current_bulb)
solutions = sp.solve(eq, current_bulb)

if solutions:
    power_dissipated = bulb_power.subs(current_bulb, solutions[0])
    print(f"Power dissipated by the bulb: {power_dissipated} W")
else:
    print("No valid solution found for current through the bulb.")

# Generate data for 3D visualization
current_range = np.linspace(0.01, 20, 100)
resistance_range = voltage_source / current_range
power_range = current_range**2 * resistance_range

# Create a Pandas DataFrame to store the data
data = pd.DataFrame({'Current (A)': current_range, 'Resistance (Ω)': resistance_range, 'Power (W)': power_range})

# Create a 3D scatter plot using Matplotlib
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(current_range, resistance_range, power_range, c='r', marker='o')

# Add labels and title
ax.set_xlabel('Current (A)')
ax.set_ylabel('Resistance (Ω)')
ax.set_zlabel('Power (W)')
ax.set_title('Power Dissipation in a Bulb (Matplotlib 3D)')

# Show the Matplotlib 3D plot
plt.show()

# Create an interactive 3D scatter plot using Plotly
fig = px.scatter_3d(data, x='Current (A)', y='Resistance (Ω)', z='Power (W)', title='Power Dissipation in a Bulb (Plotly 3D)')
fig.show()
