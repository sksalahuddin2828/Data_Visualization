import numpy as np
import matplotlib.pyplot as plt

# Given values
tension_high_E = 56.40  # N
linear_density_high_E = 3.09e-4  # kg/m

# Calculate wave speed using the formula: v = sqrt(FT / μ)
wave_speed_high_E = np.sqrt(tension_high_E / linear_density_high_E)

print(f"Wave speed on high E string: {wave_speed_high_E:.2f} m/s")

# Visualization
x = np.linspace(0, 1, 100)  # Points along the string
y = np.sin(2 * np.pi * x)  # Example wave shape

plt.figure(figsize=(10, 6))
plt.plot(x, y)
plt.title("Wave on High E String")
plt.xlabel("Position along string")
plt.ylabel("Amplitude")
plt.grid()
plt.show()


# Answer: Wave speed on high E string: 427.23 m/s
