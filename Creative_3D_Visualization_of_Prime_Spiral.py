import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from mpl_toolkits.mplot3d.art3d import Line3DCollection
import sympy as sp

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(np.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Initialize the starting point and direction
x, y = 0, 0
direction = 0

# Lists to store the coordinates of prime and non-prime points
prime_x_vals, prime_y_vals, prime_z_vals = [], [], []
non_prime_x_vals, non_prime_y_vals, non_prime_z_vals = [], [], []

# Loop to generate the spiral
num_points = 1
while num_points < 1000:
    if is_prime(num_points):
        prime_x_vals.append(x)
        prime_y_vals.append(y)
        prime_z_vals.append(num_points)
        direction += 1
    else:
        non_prime_x_vals.append(x)
        non_prime_y_vals.append(y)
        non_prime_z_vals.append(num_points)
        
    if direction % 4 == 0:
        x += 1
    elif direction % 4 == 1:
        y += 1
    elif direction % 4 == 2:
        x -= 1
    elif direction % 4 == 3:
        y -= 1
    num_points += 1

# Combine prime and non-prime points for visualization
x_vals = prime_x_vals + non_prime_x_vals
y_vals = prime_y_vals + non_prime_y_vals
z_vals = prime_z_vals + non_prime_z_vals
colors = ['red'] * len(prime_x_vals) + ['gray'] * len(non_prime_x_vals)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create a Line3DCollection for prime and non-prime points
lines = [list(zip(x_vals, y_vals, z_vals))]
line_collection = Line3DCollection(lines, colors=colors, lw=2)
ax.add_collection3d(line_collection)

# Set axis labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Prime Spiral Point')

# Set the title and customize the plot
ax.set_title('Creative 3D Visualization of Prime Spiral')

# Add dynamic effects
for angle in range(0, 360, 5):
    ax.view_init(30, angle)
    plt.draw()
    plt.pause(0.01)

plt.show()
