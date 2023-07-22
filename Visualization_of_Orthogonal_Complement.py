import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the vector space V
V = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

# Define the subspace W (a plane passing through the origin)
W = np.array([[1, 1, 0], [1, -1, 0]])

# Function to calculate the orthogonal complement of W
def orthogonal_complement(W, V):
    return np.array([v for v in V if np.all([np.dot(v, w) == 0 for w in W])])

# Calculate the orthogonal complement of W
W_orthogonal = orthogonal_complement(W, V)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot vectors in V as blue points
ax.scatter(V[:, 0], V[:, 1], V[:, 2], color='blue', label='Vector Space V')

# Plot vectors in W as red points
ax.scatter(W[:, 0], W[:, 1], W[:, 2], color='red', label='Subspace W')

# Plot vectors in W_orthogonal as green points
ax.scatter(W_orthogonal[:, 0], W_orthogonal[:, 1], W_orthogonal[:, 2], color='green', label='Orthogonal Complement W⊥')

# Add labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Visualization of Orthogonal Complement')

# Add legend
ax.legend()

# Show the plot
plt.show()
