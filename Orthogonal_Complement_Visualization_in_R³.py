import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define vectors u and v
u = np.array([2, 2, 0])
v = np.array([4, 3, 0])

# Function to calculate the projection of v onto u
def projection(v, u):
    dot_product = np.dot(v, u)
    norm_u_squared = np.linalg.norm(u)**2
    return (dot_product / norm_u_squared) * u

# Calculate the projection of v onto u
proj_u_v = projection(v, u)

# Calculate the orthogonal component
orthogonal_component = v - proj_u_v

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot vectors u and v as blue and red points, respectively
ax.scatter(*u, color='blue', s=50, label='Vector u')
ax.scatter(*v, color='red', s=50, label='Vector v')

# Plot the projection of v onto u as a green point
ax.scatter(*proj_u_v, color='green', s=50, label='Projection of v onto u')

# Plot the orthogonal component as a yellow point
ax.scatter(*orthogonal_component, color='yellow', s=50, label='Orthogonal Component of v')

# Plot the vectors (-1, 1, 0) and (0, 0, 1) spanning the orthogonal complement of W
W_orthogonal = np.array([[-1, 1, 0], [0, 0, 1]])
ax.scatter(*W_orthogonal.T, color='orange', s=50, label='Orthogonal Complement W⊥')

# Add labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Orthogonal Complement Visualization in R³')

# Add legend
ax.legend()

# Show the plot
plt.show()
