import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sympy as sp

# Constants
emf = 12.0  # EMF in volts
internal_resistance = 0.100  # Internal resistance in ohms
loads = np.linspace(0.1, 5.0, 50)  # Load resistance values from 0.1 to 5.0 ohms
internal_resistances = np.linspace(0.1, 2.0, 50)  # Internal resistance values from 0.1 to 2.0 ohms

# Calculations
V = sp.symbols('V')
I = (emf - V) / (internal_resistance + 10.0)
power = I**2 * 10.0

# Create a dataframe for results
data = {
    'Load Resistance (Ω)': [],
    'Internal Resistance (Ω)': [],
    'Terminal Voltage (V)': [],
    'Power Dissipated (W)': [],
}

for load_resistance in loads:
    for internal_resistance in internal_resistances:
        terminal_voltage = emf - I.subs(V, load_resistance)
        power_dissipated = power.subs({V: load_resistance, internal_resistance: internal_resistance})
        data['Load Resistance (Ω)'].append(load_resistance)
        data['Internal Resistance (Ω)'].append(internal_resistance)
        data['Terminal Voltage (V)'].append(float(terminal_voltage))
        data['Power Dissipated (W)'].append(float(power_dissipated))

df = pd.DataFrame(data)

# Create 3D visualization
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df['Load Resistance (Ω)'], df['Internal Resistance (Ω)'], df['Terminal Voltage (V)'],
           c=df['Power Dissipated (W)'], cmap='viridis', s=30)
ax.set_xlabel('Load Resistance (Ω)')
ax.set_ylabel('Internal Resistance (Ω)')
ax.set_zlabel('Terminal Voltage (V)')
ax.set_title('Terminal Voltage vs. Load and Internal Resistance')
plt.colorbar(ax.scatter(df['Load Resistance (Ω)'], df['Internal Resistance (Ω)'], df['Terminal Voltage (V)'],
                        c=df['Power Dissipated (W)'], cmap='viridis', s=30), label='Power Dissipated (W)')

plt.show()
