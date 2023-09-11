import numpy as np
import pandas as pd
import sympy as sp
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from sklearn.metrics import mean_squared_error
from scipy.optimize import curve_fit

# Define the given values
R = 1e3  # Ohms
C = 8e-6  # Farads
initial_voltage = 1e3  # V
target_voltage = 5e2  # V

# Calculate the time constant (τ)
tau = R * C

# Create a time array for visualization
time = np.linspace(0, 20 * tau, 1000)

# Calculate the voltage decay using the time constant
voltage_decay = initial_voltage * np.exp(-time / tau)

# Find the time it takes for the voltage to reach or drop below the target voltage
time_to_reach_target = np.where(voltage_decay <= target_voltage)[0][0] * (time[1] - time[0])

# Print the time constant and time to reach the target voltage
print(f"Time Constant (τ): {tau:.2e} seconds")
print(f"Time to Reach {target_voltage:.2e} V: {time_to_reach_target:.2e} seconds")

# Create a 3D plot of the voltage decay with artistic styling
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

X, Y = np.meshgrid(time, voltage_decay)
Z = np.sin(X) + np.cos(Y)  # Adding artistic flair

surf = ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_xlabel('Time (s)')
ax.set_ylabel('Voltage (V)')
ax.set_zlabel('Artistic Value')
ax.set_title('Voltage Decay with Artistic Styling')
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)

plt.show()

# Create a pandas DataFrame for visualization
data = pd.DataFrame({'Time (s)': time, 'Voltage (V)': voltage_decay})

# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.plot(data['Time (s)'], data['Voltage (V)'], label='Voltage Decay', color='blue')
plt.axhline(y=target_voltage, color='red', linestyle='--', label=f'{target_voltage:.2e} V')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.title('Voltage Decay Over Time')
plt.legend()
plt.grid(True)
plt.show()
