import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
cell_voltage = 3.0000  # V
load_current = 0.300  # mA
internal_resistance = 2.00  # Ohms

# Calculate the equivalent resistance of the circuit
equivalent_resistance = internal_resistance

# Calculate the voltage drop across the internal resistance
voltage_drop = load_current * equivalent_resistance / 1000  # Convert mA to A

# Calculate the output voltage
output_voltage = cell_voltage - voltage_drop

# Display the output voltage
print(f"Output Voltage: {output_voltage:.4f} V")

# Create a 3D visualization
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create a wireframe plot to represent the circuit
R = np.linspace(0, equivalent_resistance, 100)
I = np.linspace(0, load_current / 1000, 100)  # Convert mA to A
R, I = np.meshgrid(R, I)
V_drop = R * I
V_output = cell_voltage - V_drop

ax.plot_surface(R, I, V_output, cmap='viridis')

ax.set_xlabel('Equivalent Resistance (Ohms)')
ax.set_ylabel('Load Current (A)')
ax.set_zlabel('Output Voltage (V)')

plt.title('Electrical Circuit Visualization')
plt.show()
