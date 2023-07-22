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
        if len(vector) == 3:
            x, y, z = vector
            ax.quiver(0, 0, 0, x, y, z, color=color, label=label)
        elif len(vector) == 2:
            x, y = vector
            ax.quiver(0, 0, 0, x, y, 0, color=color, label=label)
    
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

# Example 2
subspace_basis_2 = [(3, 4)]
orthogonal_complement_2 = find_orthogonal_complement(subspace_basis_2)
print("Example 2 - Orthogonal Complement:", orthogonal_complement_2)

plot_vectors_3d([subspace_basis_2[0], orthogonal_complement_2[0]],
                ['r', 'g'],
                ['Subspace W', 'Orthogonal Complement W⊥'])

# Example 3
subspace_basis_3 = [(1, 0, 0), (0, 1, 0)]
orthogonal_complement_3 = find_orthogonal_complement(subspace_basis_3)
print("Example 3 - Orthogonal Complement:", orthogonal_complement_3)

plot_vectors_3d([subspace_basis_3[0], subspace_basis_3[1], orthogonal_complement_3],
                ['r', 'g', 'b'],
                ['Subspace W (1)', 'Subspace W (2)', 'Orthogonal Complement W⊥'])

# Example 4
subspace_basis_4 = [(0, 0)]
orthogonal_complement_4 = find_orthogonal_complement(subspace_basis_4)
print("Example 4 - Orthogonal Complement:", orthogonal_complement_4)

plot_vectors_3d(orthogonal_complement_4,
                ['g'],
                ['Orthogonal Complement W⊥'])

# Example 5
subspace_basis_5 = [(1, 0), (0, 1)]
orthogonal_complement_5 = find_orthogonal_complement(subspace_basis_5)
print("Example 5 - Orthogonal Complement:", orthogonal_complement_5)

plot_vectors_3d(orthogonal_complement_5,
                ['g'],
                ['Orthogonal Complement W⊥'])

# Example 6
subspace_basis_6 = [(1, 2, 3), (4, 5, 6)]
orthogonal_complement_6 = find_orthogonal_complement(subspace_basis_6)
print("Example 6 - Orthogonal Complement:", orthogonal_complement_6)

plot_vectors_3d([subspace_basis_6[0], subspace_basis_6[1], orthogonal_complement_6],
                ['r', 'g', 'b'],
                ['Subspace W (1)', 'Subspace W (2)', 'Orthogonal Complement W⊥'])

# Example 7
subspace_basis_7 = [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0)]
orthogonal_complement_7 = find_orthogonal_complement(subspace_basis_7)
print("Example 7 - Orthogonal Complement:", orthogonal_complement_7)

plot_vectors_3d([subspace_basis_7[0], subspace_basis_7[1], subspace_basis_7[2], orthogonal_complement_7],
                ['r', 'g', 'b', 'c'],
                ['Subspace W (1)', 'Subspace W (2)', 'Subspace W (3)', 'Orthogonal Complement W⊥'])

# Example 8
subspace_basis_8 = [(1, 2, 0), (2, -1, 0)]
orthogonal_complement_8 = find_orthogonal_complement(subspace_basis_8)
print("Example 8 - Orthogonal Complement:", orthogonal_complement_8)

plot_vectors_3d([subspace_basis_8[0], subspace_basis_8[1], orthogonal_complement_8],
                ['r', 'g', 'b'],
                ['Subspace W (1)', 'Subspace W (2)', 'Orthogonal Complement W⊥'])

