import numpy as np
import matplotlib.pyplot as plt

# Given values
current = 20.0e-6  # Amps
resistance = 300   # Ohms

# Calculate voltage using Ohm's law: V = I * R
voltage = current * resistance * 1e6  # Convert to μV

print("The smallest voltage that poses danger:", voltage, "μV")

# Visualization
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create a meshgrid for visualization
x = np.linspace(0, 30e-6, 100)
y = np.linspace(0, 500, 100)
X, Y = np.meshgrid(x, y)
Z = X * Y * 1e6  # Convert to μV

# Create a wireframe plot
ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
ax.set_xlabel('Current (A)')
ax.set_ylabel('Resistance (Ω)')
ax.set_zlabel('Voltage (μV)')
ax.set_title('Voltage as a Function of Current and Resistance')

plt.show()
