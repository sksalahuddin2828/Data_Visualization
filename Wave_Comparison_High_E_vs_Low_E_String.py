import numpy as np
import matplotlib.pyplot as plt

# Given values for the high E string
linear_density_high_E = 3.09e-4  # kg/m
tension_high_E = 56.40  # N

# Given values for the low E string
linear_density_low_E = 5.78e-3  # kg/m

# Calculate wave speed using the formula: v = sqrt(FT / μ)
wave_speed_high_E = np.sqrt(tension_high_E / linear_density_high_E)

print(f"Wave speed on high E string: {wave_speed_high_E:.2f} m/s")

# Calculate tension needed for the low E string to match wave speed
tension_low_E = linear_density_low_E * wave_speed_high_E**2

print(f"Tension needed for low E string: {tension_low_E:.2f} N")

# Visualization
x = np.linspace(0, 1, 100)  # Points along the string

# Example sine waves for visualization
wave_high_E = np.sin(2 * np.pi * x)
wave_low_E = 0.5 * np.sin(2 * np.pi * x)

plt.figure(figsize=(10, 6))
plt.plot(x, wave_high_E, label="High E String")
plt.plot(x, wave_low_E, label="Low E String")
plt.title("Wave Comparison: High E vs. Low E String")
plt.xlabel("Position along string")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()
plt.show()
