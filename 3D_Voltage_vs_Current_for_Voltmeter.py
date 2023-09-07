import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Define Constants
R_voltmeter = 25.0e3  # Resistance of the voltmeter in ohms
V_scale = 100.0       # Voltage scale in volts

# Calculate Sensitivity (Current for Full-Scale Deflection)
I_sensitivity = V_scale / R_voltmeter

# Define Symbolic Variables for Mathematical Expression
I, V, R = sp.symbols('I V R')

# Create Mathematical Expression
ohms_law_expr = sp.Eq(V, I * R)

# Solve for Current (I) at Full-Scale Deflection
sensitivity_equation = ohms_law_expr.subs([(V, V_scale), (R, R_voltmeter)])
sensitivity_solution = sp.solve(sensitivity_equation, I)[0]

# Convert to Numeric Value
sensitivity_numeric = float(sensitivity_solution.evalf())

# Print Sensitivity
print(f"Sensitivity of the galvanometer (Current for Full-Scale Deflection): {sensitivity_numeric} A")

# Data for Visualization
current_values = np.linspace(0, I_sensitivity * 2, 100)
voltage_values = current_values * R_voltmeter

# Create Basic 2D Plot
plt.figure(figsize=(10, 5))
plt.plot(current_values, voltage_values, label=f'Voltage vs. Current (R = {R_voltmeter} ohms)')
plt.xlabel('Current (A)')
plt.ylabel('Voltage (V)')
plt.title('Voltage vs. Current for Voltmeter')
plt.axvline(I_sensitivity, color='r', linestyle='--', label='Sensitivity Current')
plt.legend()
plt.grid(True)

# Show Sensitivity Point
plt.annotate(f'Sensitivity = {I_sensitivity} A', xy=(I_sensitivity, V_scale), xytext=(I_sensitivity + 0.0001, V_scale + 20),
             arrowprops=dict(arrowstyle='->'))
plt.show()
