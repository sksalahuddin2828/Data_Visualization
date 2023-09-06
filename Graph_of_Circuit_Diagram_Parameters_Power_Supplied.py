import numpy as np
import matplotlib.pyplot as plt

# Constants
battery_voltages = [1.58, 1.58, 1.58, 1.53]  # Voltages of alkaline cells and carbon-zinc dry cell (in V)
battery_internal_resistances = [0.0200, 0.0200, 0.0200, 0.100]  # Internal resistances (in ohms)
load_resistance = 10.0  # Load resistance (in ohms)

# Total voltage across the batteries with internal resistances
total_voltage = sum(battery_voltages) - sum(battery_internal_resistances)

# Calculate current using Ohm's law
total_resistance = sum(battery_internal_resistances) + load_resistance
current = total_voltage / total_resistance

# Calculate power supplied to the load
power_supplied = current * total_voltage

# Internal resistance calculation using optimization (e.g., scipy)
from scipy.optimize import minimize_scalar

def power_difference(internal_resistance):
    total_v = sum(battery_voltages) - internal_resistance * len(battery_voltages)
    total_r = sum(battery_internal_resistances) + load_resistance + internal_resistance * len(battery_voltages)
    current = total_v / total_r
    power = current * total_v
    return abs(power - 0.5)  # Difference from the desired power

result = minimize_scalar(power_difference)
internal_resistance_dry_cell = result.x

# Visualization
fig, ax = plt.subplots(2, 2, figsize=(12, 8))

# Circuit diagram
ax[0, 0].axis('off')
ax[0, 0].text(0.5, 0.5, "Circuit Diagram\n(Your artistic representation here)", ha='center', va='center', fontsize=12)

# Current visualization
ax[0, 1].bar(['Total Voltage', 'Total Resistance'], [total_voltage, total_resistance], color=['blue', 'red'])
ax[0, 1].set_ylabel('Value')
ax[0, 1].set_title('Circuit Parameters')

# Power supplied visualization
ax[1, 0].bar(['Current', 'Power Supplied'], [current, power_supplied], color=['green', 'orange'])
ax[1, 0].set_ylabel('Value')
ax[1, 0].set_title('Current and Power Supplied')

# Internal resistance calculation result
ax[1, 1].text(0.5, 0.5, f"Internal Resistance of Dry Cell:\n{internal_resistance_dry_cell:.4f} ohms", ha='center', va='center', fontsize=12)

plt.tight_layout()
plt.show()
