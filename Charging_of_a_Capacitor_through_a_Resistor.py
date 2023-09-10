import numpy as np
import matplotlib.pyplot as plt

# Constants
R = 1.0  # Resistance (Ohms)
C = 1.0  # Capacitance (Farads)
V0 = 0.0  # Initial voltage (Volts)

# Time constant
tau = R * C

# Time values
time_values = np.linspace(0, 5 * tau, 500)  # Adjust the time range as needed

# Calculate voltage at each time point using the charging formula
voltage_values = V0 * (1 - np.exp(-time_values / tau))

# Calculate the final voltage after two time constants
final_voltage = V0 * (1 - np.exp(-2))

# Create a 2D plot
plt.figure(figsize=(10, 6))
plt.plot(time_values, voltage_values, label=f'Final Voltage: {final_voltage:.2f} V')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.title('Charging of a Capacitor through a Resistor')
plt.legend()
plt.grid(True)
plt.show()
