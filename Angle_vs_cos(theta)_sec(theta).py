import pandas as pd
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

angles_deg = [0, 30, 45, 60, 90, 180]
angles_rad = [sp.rad(deg) for deg in angles_deg]
cos_values = [sp.cos(angle) for angle in angles_rad]
sec_values = []

for cos_val in cos_values:
    if cos_val == 0:
        sec_values.append(None)  # Use None instead of "Undefined"
    else:
        sec_values.append(1 / cos_val)

data = {
    'Angle (Degrees)': angles_deg,
    'Angle (Radians)': angles_rad,
    'cos(theta)': cos_values,
    'sec(theta)': sec_values
}

df = pd.DataFrame(data)

fig, axs = plt.subplots(1, 2, figsize=(12, 5))

# Plotting cos(theta)
axs[0].plot(df['Angle (Degrees)'], df['cos(theta)'], marker='o', linestyle='-')
axs[0].set_title('Angle vs. cos(theta)')
axs[0].set_xlabel('Angle (Degrees)')
axs[0].set_ylabel('cos(theta)')

# Plotting sec(theta) while excluding 'Undefined' values
sec_values_numeric = [val if val is not None else float('nan') for val in df['sec(theta)']]
axs[1].plot(df['Angle (Degrees)'], sec_values_numeric, marker='o', linestyle='-')
axs[1].set_title('Angle vs. sec(theta)')
axs[1].set_xlabel('Angle (Degrees)')
axs[1].set_ylabel('sec(theta)')

plt.tight_layout()
plt.show()
