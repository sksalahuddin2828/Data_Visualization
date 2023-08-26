import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a time array
t = np.linspace(0, 2 * np.pi, 100)
# Create voltage and current arrays
V = np.sin(t)
I = np.cos(t)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(t, V, I)

ax.set_xlabel('Time')
ax.set_ylabel('Voltage')
ax.set_zlabel('Current')

plt.show()
