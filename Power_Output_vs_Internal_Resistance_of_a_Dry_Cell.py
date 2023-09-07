import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Constants
V = 1.54  # Voltage of the dry cell (V)
P = 1.00  # Power supplied to the bulb (W)
R_bulb = 15.0  # Resistance of the bulb (Ω)

# Calculate internal resistance using the power formula
R_internal = sp.symbols('R_internal')
equation = sp.Eq(P, V**2 / (R_internal + R_bulb))
internal_resistance_solution = sp.solve(equation, R_internal)

# Convert the SymPy solutions to numerical values
internal_resistance_values = [float(sol) for sol in internal_resistance_solution]

# Typical range of internal resistance for dry cells
typical_internal_resistance = np.linspace(0.1, 0.5, 100)

# Calculate corresponding power output values for the typical internal resistances
power_output_values = [P / (V**2 / (R + R_bulb)) for R in typical_internal_resistance]

# Visualize the result
plt.figure(figsize=(10, 6))
plt.plot(typical_internal_resistance, power_output_values, label='Power vs Internal Resistance')
plt.scatter(internal_resistance_values, [P / (V**2 / (R + R_bulb)) for R in internal_resistance_values], color='red', marker='o', label='Calculated Internal Resistance')
plt.xlabel('Internal Resistance (Ω)')
plt.ylabel('Power Output (W)')
plt.title('Power Output vs Internal Resistance of a Dry Cell')
plt.legend()
plt.grid()

# Show the visualization
plt.show()
