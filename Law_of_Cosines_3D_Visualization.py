import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define side lengths
a_val = 4
b_val = 3

# Define angle values
gamma_vals = np.linspace(0, np.pi, 100)
c_vals = np.sqrt(a_val**2 + b_val**2 - 2 * a_val * b_val * np.cos(gamma_vals))

# Create 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the curve
ax.plot(gamma_vals, a_val * np.ones_like(gamma_vals), c_vals, label='Side c')

# Set labels and title
ax.set_xlabel('Angle (γ)')
ax.set_ylabel('Side a')
ax.set_zlabel('Side c')
ax.set_title('Law of Cosines 3D Visualization')

# Show the plot
plt.show()
