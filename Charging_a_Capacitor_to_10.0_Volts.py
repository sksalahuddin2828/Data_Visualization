import numpy as np
import matplotlib.pyplot as plt

# Define capacitor parameters
C = 1.0  # Capacitance (in Farads)
R = 1.0  # Resistance (in Ohms)
V_emf = 10.0  # EMF (in Volts)

# Define the voltage function during charging
def voltage(t):
    return V_emf * (1 - np.exp(-t / (R * C)))

# Create a time array
t = np.linspace(0, 5 * R * C, 1000)

# Calculate the voltage across the capacitor at each time point
V = voltage(t)

# Find the time it takes for the voltage to reach V_emf (if it ever does)
charging_time = None
if np.any(V >= V_emf):
    charging_time = t[np.where(V >= V_emf)[0][0]]

# Plot the voltage vs. time
plt.plot(t, V)
plt.xlabel('Time (seconds)')
plt.ylabel('Voltage (Volts)')
plt.title(f'Charging a Capacitor to {V_emf} Volts')
plt.grid(True)
plt.show()

if charging_time is not None:
    print(f'Time taken to reach {V_emf} Volts: {charging_time:.2f} seconds')
else:
    print(f'The capacitor never reaches {V_emf} Volts within the specified time range.')
