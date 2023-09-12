import numpy as np

def discharge_time(R, C, V0):
    return -R * C * np.log(0.0001)  # Using a small value instead of zero

R = 1000  # Ohms
C = 0.001  # Farads
V0 = 10  # Initial voltage (e.g., 10 volts)

time_to_zero = discharge_time(R, C, V0)
print(f"Time to reach zero voltage: {time_to_zero} seconds")

import numpy as np
import matplotlib.pyplot as plt

# Define parameters
R = 1000  # Ohms
C = 0.001  # Farads
V0 = 10  # Initial voltage (e.g., 10 volts)
tau = R * C  # Time constant

# Create time values
time = np.linspace(0, 5 * tau, 1000)  # Adjust the time range as needed

# Calculate potential difference across the resistor
V_resistor = V0 * np.exp(-time / tau)

# Calculate current
current = V_resistor / R

# Plot potential difference vs. time
plt.figure(figsize=(12, 4))
plt.subplot(121)
plt.plot(time, V_resistor, label='Potential Difference')
plt.xlabel('Time (s)')
plt.ylabel('Potential Difference (V)')
plt.title('Potential Difference vs. Time')
plt.legend()

# Plot current vs. time
plt.subplot(122)
plt.plot(time, current, label='Current')
plt.xlabel('Time (s)')
plt.ylabel('Current (A)')
plt.title('Current vs. Time')
plt.legend()

plt.tight_layout()
plt.show()
