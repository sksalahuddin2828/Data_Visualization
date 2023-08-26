import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a figure and a 3D subplot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create data points for the plot
current_values = np.linspace(100, 1000, 10)
voltage_values = np.linspace(100, 1000, 10)
current_values, voltage_values = np.meshgrid(current_values, voltage_values)
power_loss = (current_values**2 * R) / (current_values * voltage_values)

# Create the 3D surface plot
surf = ax.plot_surface(current_values, voltage_values, power_loss, cmap='viridis')

# Customize the plot
ax.set_xlabel('Current (A)')
ax.set_ylabel('Voltage (V)')
ax.set_zlabel('Power Loss (W)')
ax.set_title('Power Loss in Transmission Lines')

# Add a colorbar
fig.colorbar(surf)

# Show the plot
plt.show()
