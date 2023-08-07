import numpy as np
import matplotlib.pyplot as plt

# Given wave function parameters
A = 0.5  # Amplitude
k = 2 * np.pi / 5  # Wave number
w = 2 * np.pi / 2  # Angular frequency
phi = np.pi / 4  # Initial phase

# Calculate characteristics of the wave
period = 2 * np.pi / w
frequency = 1 / period
wavelength = 2 * np.pi / k

print("Amplitude:", A)
print("Period:", period)
print("Frequency:", frequency)
print("Wavelength:", wavelength)

# Visualization of the sinusoidal wave
x_values = np.linspace(0, 10, 400)
y_values = A * np.sin(k * x_values - w * 0 + phi)

plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label='y(x,t) = Asin(kx - ωt + ϕ)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Sinusoidal Wave Characteristics')
plt.legend()
plt.grid(True)
plt.show()
