import numpy as np
import matplotlib.pyplot as plt

# Define parameters
initial_voltage = 1000.0  # Initial voltage across the capacitor (V)
bleeder_resistor = 1000.0  # Bleeder resistor resistance (ohms)
capacitance = 0.001  # Capacitance (farads)

# Calculate the time constant
time_constant = bleeder_resistor * capacitance

# Time values
time = np.linspace(0, 10 * time_constant, 1000)

# Calculate voltage across the capacitor over time
voltage = initial_voltage * np.exp(-time / time_constant)

# Create a 2D plot of the discharge curve
plt.figure(figsize=(10, 6))
plt.plot(time, voltage)
plt.title('Capacitor Discharge Curve')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.grid(True)

# Create a 3D plot (a simple example)
# This can be customized further for a more creative visualization
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot(time, voltage, np.zeros_like(time), lw=2)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Voltage (V)')
ax.set_zlabel('Z')
ax.set_title('3D Visualization of Capacitor Discharge')
plt.show()
