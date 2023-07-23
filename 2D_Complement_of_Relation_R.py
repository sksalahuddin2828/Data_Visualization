import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def visualize_relation(relation_matrix, set_name, title):
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
    
    plt.title(title)
    plt.legend()
    plt.show()

def complement_relation(relation_matrix):
    return np.logical_not(relation_matrix)

# Example 1
A = {1, 2, 3, 4}
B = {8, 9}
relation_example1 = np.array([[1, 1, 1, 0], [0, 1, 1, 1]])
dom_r = [1, 2]
ran_r = [8, 9]
visualize_relation(relation_example1, A, "Relation R")
print("DOM(R):", dom_r)
print("RAN(R):", ran_r)

# Example 2
X = {1, 2, 3}
Y = {8, 9}
relation_example2 = np.array([[1, 0], [1, 0], [0, 1]])
complement_example2 = complement_relation(relation_example2)
dom_r2 = [1, 2, 3]
ran_r2 = [8, 9]
visualize_relation(relation_example2, X, "Relation R")
visualize_relation(complement_example2, X, "Complement of Relation R")
print("DOM(R):", dom_r2)
print("RAN(R):", ran_r2)

# Example 3
X = {1, 2, 3}
Y = {8, 9}
relation_example3 = np.array([[0, 1], [1, 0], [0, 1]])
complement_example3 = complement_relation(relation_example3)
dom_r3 = [1, 2, 3]
ran_r3 = [8, 9]
visualize_relation(relation_example3, X, "Relation R")
visualize_relation(complement_example3, X, "Complement of Relation R")
print("DOM(R):", dom_r3)
print("RAN(R):", ran_r3)
