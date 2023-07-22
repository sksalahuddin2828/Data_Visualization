import numpy as np
import matplotlib.pyplot as plt

# Define the vector space V (R²)
V = np.array([[1, 0], [0, 1]])

# Define the subspace W spanned by (3, 4)
W = np.array([[3, 4]])

# Function to calculate the orthogonal complement of W
def orthogonal_complement(W, V):
    return np.array([v for v in V if np.all([np.dot(v, w) == 0 for w in W])])

# Calculate the orthogonal complement of W
W_orthogonal = orthogonal_complement(W, V)

# Convert W_orthogonal to a 2-dimensional array for visualization
W_orthogonal_2d = W_orthogonal.reshape(-1, 2)

# Create a 2D plot
plt.figure()

# Plot vectors in V as blue points
plt.scatter(V[:, 0], V[:, 1], color='blue', label='Vector Space V')

# Plot vectors in W as red points
plt.scatter(W[:, 0], W[:, 1], color='red', label='Subspace W')

# Plot vectors in W_orthogonal as green points
plt.scatter(W_orthogonal_2d[:, 0], W_orthogonal_2d[:, 1], color='green', label='Orthogonal Complement W⊥')

# Add labels and title
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Visualization of Orthogonal Complement in R²')

# Add legend
plt.legend()

# Show the plot
plt.grid()
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.show()
