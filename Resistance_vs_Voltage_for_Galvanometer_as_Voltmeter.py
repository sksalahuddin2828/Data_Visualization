import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# Constants
galvanometer_sensitivity = 100e-6  # 100 μA
galvanometer_resistance = 10.0  # 10.0 Ω

# (a) Full-scale reading of 300 V
full_scale_reading_a = 300.0  # 300 V

# Calculate resistance needed for (a)
def calculate_resistance_a(full_scale_voltage_a):
    resistance_a = (full_scale_voltage_a / galvanometer_sensitivity) - galvanometer_resistance
    return resistance_a

resistance_a = calculate_resistance_a(full_scale_reading_a)

# (b) Full-scale reading of 0.300 V
full_scale_reading_b = 0.300  # 0.300 V

# Calculate resistance needed for (b)
def calculate_resistance_b(full_scale_voltage_b):
    resistance_b = (full_scale_voltage_b / galvanometer_sensitivity) - galvanometer_resistance
    return resistance_b

resistance_b = calculate_resistance_b(full_scale_reading_b)

# Data Visualization (Optional: 3D plot)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create a 3D plot showing the resistance required for both scenarios
voltages = np.linspace(0.001, 400, 100)  # Varying voltages from 0.001V to 400V
resistance_values_a = [(v / galvanometer_sensitivity) - galvanometer_resistance for v in voltages]
resistance_values_b = [(v / galvanometer_sensitivity) - galvanometer_resistance for v in voltages]

ax.plot(voltages, resistance_values_a, resistance_values_b)

ax.set_xlabel('Voltage (V)')
ax.set_ylabel('Resistance for (a) (Ω)')
ax.set_zlabel('Resistance for (b) (Ω)')

plt.title('Resistance vs. Voltage for Galvanometer as Voltmeter')
plt.show()

# Print the results
print(f"Required resistance for (a) with a {full_scale_reading_a} V full-scale reading: {resistance_a:.2f} Ω")
print(f"Required resistance for (b) with a {full_scale_reading_b} V full-scale reading: {resistance_b:.2f} Ω")
