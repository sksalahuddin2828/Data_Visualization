import numpy as np
import matplotlib.pyplot as plt

# Generate time values
t = np.linspace(0, 2*np.pi, 1000)

# Simulate AC voltages and currents
V = 220 * np.sin(2*np.pi*50*t)
I = 2 * np.sin(2*np.pi*50*t - np.pi/6)  # Phase difference of 30 degrees

# Plot Lissajous figure
plt.figure(figsize=(8, 6))
plt.plot(V, I, color='blue')
plt.title('Lissajous Figure')
plt.xlabel('Voltage (V)')
plt.ylabel('Current (A)')
plt.grid()
plt.show()

# Create phasor diagram
plt.figure(figsize=(8, 6))
plt.plot([0, np.max(V)], [0, 0], color='red', label='Voltage')
plt.plot([0, np.max(I)], [0, 0], color='blue', label='Current')
plt.plot([0, np.max(V)], [0, np.max(I)], color='purple', label='Impedance')
plt.legend()
plt.title('Phasor Diagram')
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.grid()
plt.show()
