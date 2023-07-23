import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def visualize_relation(relation_matrix, set_name):
    x, y = np.where(relation_matrix)
    z = np.ones_like(x)
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    ax.scatter(x, y, z, s=400, marker='o', label='Relation')
    
    ax.set_xticks(np.arange(len(set_name)))
    ax.set_yticks(np.arange(len(set_name)))
    ax.set_xticklabels(set_name)
    ax.set_yticklabels(set_name)
    
    ax.set_xlabel('Element in Set A')
    ax.set_ylabel('Element in Set B')
    ax.set_zlabel('Relation')
    
    plt.title('Binary Relation Visualization')
    plt.legend()
    plt.show()

# Example 1
A = {1, 2}
B = {1, 2}
relation_example1 = np.array([[0, 0], [1, 1]])
visualize_relation(relation_example1, A)

# Example 2
m = 2
n = 3
relation_example2 = np.random.randint(2, size=(m, n))
visualize_relation(relation_example2, f"Set A (Size: {m})")

# Example 3
A = {1, 2}
relation_example3 = np.random.randint(2, size=(len(A), len(A)))
visualize_relation(relation_example3, A)
