import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def find_orthogonal_complement(subspace_basis):
    A = np.array(subspace_basis).T
    Q, _ = np.linalg.qr(A)
    orthogonal_complement = []
    for col in Q.T:
        orthogonal_complement.append(tuple(col))
    return orthogonal_complement

def plot_vectors_3d(vectors, colors, labels):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    for vector, color, label in zip(vectors, colors, labels):
        ax.quiver(0, 0, 0, *vector, color=color, label=label)
    
    ax.set_xlim([-5, 5])
    ax.set_ylim([-5, 5])
    ax.set_zlim([-5, 5])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.legend()
    plt.show()

# Example 1
subspace_basis_1 = [(1, 1, 0)]
orthogonal_complement_1 = find_orthogonal_complement(subspace_basis_1)
print("Example 1 - Orthogonal Complement:", orthogonal_complement_1)

# Check if the orthogonal complement contains only one vector
if len(orthogonal_complement_1) == 1:
    plot_vectors_3d([subspace_basis_1[0], orthogonal_complement_1[0]],
                    ['r', 'g'],
                    ['Subspace W', 'Orthogonal Complement W⊥'])
else:
    plot_vectors_3d([subspace_basis_1[0], orthogonal_complement_1[0], orthogonal_complement_1[1]],
                    ['r', 'g', 'b'],
                    ['Subspace W', 'Orthogonal Complement W⊥ (1)', 'Orthogonal Complement W⊥ (2)'])



# Answer: Example 1 - Orthogonal Complement: [(-0.7071067811865472, -0.7071067811865475, -0.0)]
