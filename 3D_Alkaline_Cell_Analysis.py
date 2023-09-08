import numpy as np
import matplotlib.pyplot as plt

# Constants
emf = 1.585  # EMF of the alkaline cell in volts
internal_resistance = 0.100  # Internal resistance in ohms
external_resistance = 1000.0  # External resistance in ohms

# (a) Calculate the current flowing through the circuit
current = emf / (internal_resistance + external_resistance)

# (b) Calculate the terminal voltage
terminal_voltage = emf - current * internal_resistance

# (c) Calculate the ratio of measured terminal voltage to EMF
ratio = terminal_voltage / emf

# Create a 3D plot to visualize the scenario
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the EMF, internal resistance, and external resistance
ax.bar(['EMF', 'Internal Resistance', 'External Resistance'], [emf, internal_resistance, external_resistance], zdir='y', width=0.3)

# Plot the current and terminal voltage
ax.bar(['Current', 'Terminal Voltage'], [current, terminal_voltage], zdir='y', width=0.3, color='r')

# Set labels and title
ax.set_xlabel('Components')
ax.set_ylabel('Values')
ax.set_zlabel('Magnitude')
ax.set_title('Alkaline Cell Analysis')

# Show the plot
plt.show()

# Display results
print(f'(a) Current Flowing: {current} A')
print(f'(b) Terminal Voltage: {terminal_voltage} V')
print(f'(c) Ratio of Measured Terminal Voltage to EMF: {ratio}')
