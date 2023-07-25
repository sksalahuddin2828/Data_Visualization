import numpy as np
import matplotlib.pyplot as plt
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

# Loop to generate the spiral
num_points = 1
while num_points < 1000:
    if is_prime(num_points):
        direction += 1
    if direction % 4 == 0:
        x += 1
    elif direction % 4 == 1:
        y += 1
    elif direction % 4 == 2:
        x -= 1
    elif direction % 4 == 3:
        y -= 1
    num_points += 1

print(f"The coordinates of the 1000th point are: ({x}, {y})")

# Generate the spiral coordinates
x_vals = [0]
y_vals = [0]

num_points = 1
while num_points < 1000:
    if is_prime(num_points):
        direction += 1
    if direction % 4 == 0:
        x += 1
    elif direction % 4 == 1:
        y += 1
    elif direction % 4 == 2:
        x -= 1
    elif direction % 4 == 3:
        y -= 1
    x_vals.append(x)
    y_vals.append(y)
    num_points += 1

# Create the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x_vals, y_vals, range(1000), c='b', marker='o')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Prime Spiral Point')
ax.set_title('3D Visualization of Prime Spiral')
plt.show()

