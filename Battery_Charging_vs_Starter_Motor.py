import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
emf = 12.0  # Volts
internal_resistance = 0.050  # Ohms
current_charge = 60.0  # Amperes
current_starter = 60.0  # Amperes

# (a) Potential difference across terminals during charging
voltage_charge = emf - current_charge * internal_resistance

# (b) Rate of thermal energy dissipation during charging
thermal_energy_charge = current_charge**2 * internal_resistance

# (c) Rate of electric energy conversion to chemical energy during charging
electric_to_chemical_charge = voltage_charge * current_charge

# (d) Potential difference and thermal energy during starter motor use
voltage_starter = emf - current_starter * internal_resistance
thermal_energy_starter = current_starter**2 * internal_resistance

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Scatter plot points
points = ['Charging', 'Starter']
values = [voltage_charge, voltage_starter]
thermal_values = [thermal_energy_charge, thermal_energy_starter]

ax.scatter([0, 1], values, thermal_values, c='b', marker='o')

# Add labels and title
ax.set_xlabel('Process')
ax.set_ylabel('Potential Difference (Volts)')
ax.set_zlabel('Thermal Energy Dissipation (Watts)')
plt.title('Battery Charging vs. Starter Motor')

# Annotate points with process names
for i, txt in enumerate(points):
    ax.text(i, values[i], thermal_values[i], txt, ha='right')

# Show the 3D plot
plt.show()
