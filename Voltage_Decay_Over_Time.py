import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sympy as sp

# Constants
V0 = 10000  # Initial voltage in volts
decay_factor = 0.368
time_intervals = np.array([8.0, 16.0, 24.0])  # Time intervals in milliseconds

# Calculate voltage at each time interval
voltages = [V0]
for t in time_intervals:
    voltage = V0 * (decay_factor ** (t / 8.0))
    voltages.append(voltage)

# Create a pandas DataFrame to store the data
data = pd.DataFrame({'Time (ms)': [0] + list(time_intervals), 'Voltage (V)': voltages})

# Print the data
print(data)

# Plot the voltage decay over time
plt.figure(figsize=(10, 6))
plt.plot(data['Time (ms)'], data['Voltage (V)'], marker='o')
plt.title('Voltage Decay Over Time')
plt.xlabel('Time (ms)')
plt.ylabel('Voltage (V)')
plt.grid(True)
plt.show()

# Create a 3D visualization
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot(data['Time (ms)'], data['Voltage (V)'], np.zeros(len(data)), marker='o')
ax.set_xlabel('Time (ms)')
ax.set_ylabel('Voltage (V)')
ax.set_zlabel('Zero')
ax.set_title('3D Voltage Decay')
plt.show()

# Symbolic calculation using sympy
t_symbolic = sp.symbols('t')
voltage_symbolic = V0 * (decay_factor ** (t_symbolic / 8.0))
solution = sp.solve(voltage_symbolic - V0 * 0.5, t_symbolic)
print(f'Time for voltage to reach 50% of initial value: {solution[0]} ms')
