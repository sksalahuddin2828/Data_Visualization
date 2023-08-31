import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Generate data
R1_values = np.linspace(1, 1000, 50)
R2_values = np.linspace(1, 100, 50)
R1, R2 = np.meshgrid(R1_values, R2_values)
series_resistances = R1 + R2
parallel_resistances = 1 / (1 / R1 + 1 / R2)

# Plot series resistance
ax.plot_surface(R1, R2, series_resistances, cmap='viridis')
ax.set_xlabel('R1')
ax.set_ylabel('R2')
ax.set_zlabel('Series Resistance')
ax.set_title('Series Resistance Visualization')

plt.show()
