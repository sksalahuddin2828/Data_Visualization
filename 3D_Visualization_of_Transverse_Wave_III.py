import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Given wave function parameters
A = 0.2
k = 6.28
omega = 1.57

# Calculate wave characteristics
wavelength = 2 * np.pi / k
period = 2 * np.pi / omega
wave_speed = omega / k

# Generate x and t values
x_values = np.linspace(0, 10, 200)
t_values = np.linspace(0, 10, 200)

# Create a meshgrid for 3D visualization
X, T = np.meshgrid(x_values, t_values)

# Calculate y values for 3D visualization
y_values = A * np.sin(k * X - omega * T)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, T, y_values, cmap='viridis')

ax.set_title("3D Visualization of Transverse Wave")
ax.set_xlabel("Position (x)")
ax.set_ylabel("Time (t)")
ax.set_zlabel("Amplitude (y)")

plt.show()

print("Amplitude:", A)
print("Wavelength:", wavelength)
print("Period:", period)
print("Wave Speed:", wave_speed)
