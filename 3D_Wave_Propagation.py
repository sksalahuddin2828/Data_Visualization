import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
A = 1.0
k = 2.0
ω = 3.0
ϕ = np.pi/4.0

# Generate data
x = np.linspace(0, 10, 100)  # Spatial coordinates
t = np.linspace(0, 5, 50)    # Time coordinates

X, T = np.meshgrid(x, t)     # Meshgrid for 3D plot

# Compute wave function
y = A * np.sin(k * X - ω * T + ϕ)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, T, y, cmap='viridis')

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Time')
ax.set_zlabel('Amplitude')
ax.set_title('Wave Propagation')

plt.show()
