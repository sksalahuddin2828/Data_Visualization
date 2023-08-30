import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Define short circuit resistance equation
def short_circuit_resistance(power, voltage):
    return voltage ** 2 / power

# Create example data
power_data = np.linspace(10, 5000, 100)
voltage_data = np.full_like(power_data, 220)  # Using a constant voltage for demonstration
resistance_data = short_circuit_resistance(power_data, voltage_data)
power_dissipation_data = power_data * resistance_data / 1000

# Create a DataFrame
df = pd.DataFrame({'Power (kW)': power_data,
                   'Resistance (Ω)': resistance_data,
                   'Power Dissipation (kW)': power_dissipation_data})

# Create a 2D plot with annotations and theory explanation
fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('Power (kW)')
ax1.set_ylabel('Resistance (Ω)', color=color)
ax1.plot(power_data, resistance_data, color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax1.annotate('Short Circuit Resistance\nEquation: R = V² / P', xy=(2000, 300), fontsize=10,
             bbox=dict(boxstyle="round,pad=0.3", edgecolor="gray", facecolor="white"))

ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Power Dissipation (kW)', color=color)
ax2.plot(power_data, power_dissipation_data, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()
plt.title('Short Circuit Resistance and Power Dissipation')
plt.show()
