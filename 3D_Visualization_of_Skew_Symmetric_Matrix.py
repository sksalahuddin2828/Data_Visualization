import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate a random skew-symmetric matrix
def generate_skew_symmetric_matrix(size):
    mat = np.random.rand(size, size)
    skew_symmetric = (mat - mat.T) / 2
    return skew_symmetric

# Verify if a matrix is skew-symmetric
def is_skew_symmetric(matrix):
    return np.allclose(matrix, -matrix.T)

# Visualize a skew-symmetric matrix
def visualize_skew_symmetric(matrix):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    size = matrix.shape[0]

    for i in range(size):
        for j in range(size):
            if i != j:
                ax.quiver(i, j, 0, matrix[i, j], matrix[j, i], 0, color='b')

    ax.set_xlim([0, size])
    ax.set_ylim([0, size])
    ax.set_zlim([-1, 1])
    ax.set_xlabel('Row')
    ax.set_ylabel('Column')
    ax.set_zlabel('Value')
    plt.title('Visualization of Skew-Symmetric Matrix')
    plt.show()

# Example usage
size = 3
matrix = generate_skew_symmetric_matrix(size)
print("Generated Matrix:")
print(matrix)
print("Is Skew-Symmetric:", is_skew_symmetric(matrix))

visualize_skew_symmetric(matrix)
