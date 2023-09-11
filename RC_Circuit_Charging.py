import numpy as np
import matplotlib.pyplot as plt

# Step 1: Define parameters for the RC circuit
R = 1e3  # Resistance in ohms
C = 1e-6  # Capacitance in farads
time_constant = R * C  # RC time constant

# Step 2: Generate time values
t = np.linspace(0, 5 * time_constant, 1000)

# Step 3: Calculate voltage across the capacitor
voltage = 5 * (1 - np.exp(-t / time_constant))  # Voltage equation for charging capacitor

# Step 4: Create a 3D visualization
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot voltage vs. time
ax.plot(t, voltage, zs=0, zdir='z', label='Voltage vs. Time')
ax.set_xlabel('Time (s)')
ax.set_ylabel('Voltage (V)')
ax.set_zlabel('')

# Step 5: Show the plot
plt.legend()
plt.title('RC Circuit Charging')
plt.show()
