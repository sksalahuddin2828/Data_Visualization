import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Example ordered triple
ordered_triple = [(1, 2, 3), (2, 3, 4), (3, 4, 5), (4, 5, 6)]

# Create 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for x, y, z in ordered_triple:
    ax.scatter(x, y, z, c='r', marker='o')

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

plt.show()
