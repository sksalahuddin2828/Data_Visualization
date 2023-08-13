import numpy as np
import matplotlib.pyplot as plt

# Create two matrices
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

# Perform matrix multiplication
C = np.dot(A, B)

# Visualize matrices and their multiplication
plt.figure(figsize=(10, 4))

plt.subplot(131)
plt.imshow(A, cmap='viridis')
plt.title('Matrix A')

plt.subplot(132)
plt.imshow(B, cmap='plasma')
plt.title('Matrix B')

plt.subplot(133)
plt.imshow(C, cmap='magma')
plt.title('Matrix A * B')

plt.tight_layout()
plt.show()
