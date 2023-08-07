import numpy as np
import matplotlib.pyplot as plt

# Given wave function parameters
A = 0.2
k = 6.28
omega = 1.57

# Calculate wavelength and period
wavelength = 2 * np.pi / k
period = 2 * np.pi / omega

# Calculate speed of the wave
wave_speed = omega / k

# Generate x values
x_values = np.linspace(0, 2 * np.pi, 100)

# Generate y values using the wave function
y_values = A * np.sin(k * x_values - omega * 0)

# Create a basic plot of the wave
plt.plot(x_values, y_values)
plt.title("Transverse Wave on a String")
plt.xlabel("Position (x)")
plt.ylabel("Amplitude (y)")
plt.show()

print("Amplitude:", A)
print("Wavelength:", wavelength)
print("Period:", period)
print("Wave Speed:", wave_speed)
