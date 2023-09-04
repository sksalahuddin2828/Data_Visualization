import numpy as np
import pandas as pd
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define symbolic variables
emf, Rload, r, I, V = sp.symbols('emf Rload r I V')

# Define equations
I_eq = sp.Eq(I, emf / (Rload + r))
V_eq = sp.Eq(V, emf - I * r)

# Create a list of Rload values to analyze
Rload_values = np.linspace(0.1, 10.0, 100)

# Initialize lists to store results
current_values = []
voltage_values = []

# Create a lambdified function to calculate voltage numerically
calc_voltage = sp.lambdify((emf, r, I), V_eq.rhs)

# Calculate current and voltage for each Rload value
for R in Rload_values:
    current = I_eq.subs({emf: 12.0, r: 0.1, Rload: R}).rhs  # Extract numerical value
    voltage = calc_voltage(12.0, 0.1, current)
    current_values.append(current)
    voltage_values.append(voltage)

# Create a DataFrame to store the results
df = pd.DataFrame({'Rload': Rload_values, 'Current': current_values, 'Voltage': voltage_values})

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('Rload (Ω)')
ax.set_ylabel('Current (A)')
ax.set_zlabel('Voltage (V)')
ax.set_title('Battery Characteristics')

# Plot the 3D data points
ax.scatter(df['Rload'], df['Current'], df['Voltage'], c='b', marker='o')

# Show the 3D plot
plt.show()
