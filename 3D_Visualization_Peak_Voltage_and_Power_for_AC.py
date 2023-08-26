import numpy as np
import pandas as pd
import plotly.express as px
import sympy as sp
import matplotlib.pyplot as plt

# Given values
Vrms = 120  # V
Pave = 60.0  # W

# Calculate peak voltage (V0)
V0 = np.sqrt(2) * Vrms

# Calculate peak power (P0)
P0 = 2 * Pave

# Create a plot for AC voltage waveform
time = np.linspace(0, 1, 1000)
voltage = V0 * np.sin(2 * np.pi * time)
plt.figure(figsize=(10, 5))
plt.plot(time, voltage)
plt.title('AC Voltage Waveform')
plt.xlabel('Time')
plt.ylabel('Voltage (V)')
plt.grid()
plt.show()

# Create a bar chart for power variations
power_labels = ['0 W', '120 W']
power_values = [0, P0]
plt.bar(power_labels, power_values, color=['blue', 'orange'])
plt.title('Power Variation')
plt.xlabel('Power')
plt.ylabel('Value')
plt.show()

# Create a 3D surface plot using matplotlib
I0_vals = np.linspace(0, 2, 100)
V0_vals = np.linspace(0, V0, 100)
I0, V0 = np.meshgrid(I0_vals, V0_vals)
P0_surface = 2 * I0 * V0

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(I0, V0, P0_surface, cmap='viridis')
ax.set_title('Peak Power Surface')
ax.set_xlabel('Peak Current (I0)')
ax.set_ylabel('Peak Voltage (V0)')
ax.set_zlabel('Peak Power (P0)')
plt.show()
