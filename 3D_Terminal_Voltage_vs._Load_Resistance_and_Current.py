import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Given values
emf = 12.0  # V
load_resistance = np.linspace(1, 20, 100)  # Vary load resistance from 1 to 20 ohms
internal_resistance = 0.1  # Ohms

# Calculate current and terminal voltage
current = emf / (load_resistance + internal_resistance)
terminal_voltage = emf - current * internal_resistance

# Create a DataFrame to store the data
data = pd.DataFrame({'Load Resistance': load_resistance, 'Current': current, 'Terminal Voltage': terminal_voltage})

# Basic 3D Visualization
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(load_resistance, current, terminal_voltage, c=terminal_voltage, cmap='viridis', marker='o')
ax.set_xlabel('Load Resistance (Ohms)')
ax.set_ylabel('Current (A)')
ax.set_zlabel('Terminal Voltage (V)')
ax.set_title('Terminal Voltage vs. Load Resistance and Current')

plt.show()
