import numpy as np
import matplotlib.pyplot as plt

# Generate sample data
current = np.linspace(0, 10, 100)
resistance = 2.0
power = current ** 2 * resistance
temperature_rise = power * 0.05  # A simple relationship for demonstration

# Create a scatter plot of power dissipation vs current
plt.figure(figsize=(10, 6))
plt.scatter(current, power, c=temperature_rise, cmap='coolwarm', marker='o')
plt.colorbar(label='Temperature Rise')
plt.xlabel('Current (A)')
plt.ylabel('Power Dissipation (W)')
plt.title('Power Dissipation vs Current in an Electric Circuit')
plt.grid(True)
plt.show()
