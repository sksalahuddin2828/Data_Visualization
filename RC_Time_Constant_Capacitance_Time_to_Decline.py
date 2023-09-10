import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Given parameters
RC = 10e-3  # RC time constant in seconds
C = 8e-6  # Capacitance in Farads
initial_voltage = 12e3  # Initial voltage in Volts
final_voltage = 6e2  # Final voltage in Volts

# Part (a): Calculate the resistance
R = RC / C

# Part (b): Calculate the time to decline to the final voltage
time_to_decline = RC * np.log(initial_voltage / final_voltage)

# Create a time array
t = np.linspace(0, 10 * time_to_decline, 1000)

# Calculate voltage decay
voltage = initial_voltage * np.exp(-t / RC)

# Visualization: Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create a grid of RC values and Capacitance values
RC_values = np.linspace(1e-3, 20e-3, 100)
C_values = np.linspace(1e-6, 20e-6, 100)
RC_values, C_values = np.meshgrid(RC_values, C_values)

# Calculate corresponding resistance values
R_values = RC_values / C_values

# Calculate time to decline for each combination of RC and C
time_values = RC_values * np.log(initial_voltage / final_voltage)

# Plot the 3D surface
ax.plot_surface(RC_values, C_values, time_values, cmap='viridis')
ax.set_xlabel('RC Time Constant (s)')
ax.set_ylabel('Capacitance (F)')
ax.set_zlabel('Time to Decline (s)')

# Show the plot
plt.show()

# Print the results
print(f"Part (a): The resistance of the path through the patient is {R:.2f} ohms.")
print(f"Part (b): It takes {time_to_decline:.2f} seconds for the voltage to decline to {final_voltage} V.")
