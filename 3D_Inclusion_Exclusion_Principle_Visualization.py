import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Sets A, B, and C
A = set([1, 2, 3, 4, 5])
B = set([4, 5, 6, 7, 8])
C = set([6, 7, 8, 9, 10])

# Calculate n(A), n(B), n(C)
n_A = len(A)
n_B = len(B)
n_C = len(C)

# Calculate n(A ∩ B), n(A ∩ C), n(B ∩ C), n(A ∩ B ∩ C)
n_A_int_B = len(A.intersection(B))
n_A_int_C = len(A.intersection(C))
n_B_int_C = len(B.intersection(C))
n_A_int_B_int_C = len(A.intersection(B).intersection(C))

# Calculate n(A ∪ B ∪ C) using inclusion-exclusion principle
n_A_union_B_union_C = n_A + n_B + n_C - n_A_int_B - n_A_int_C - n_B_int_C + n_A_int_B_int_C

# 3D Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create points for the three sets
points_A = np.array([[x, 0, 0] for x in A])
points_B = np.array([[0, y, 0] for y in B])
points_C = np.array([[0, 0, z] for z in C])

# Plot the points for each set
ax.scatter(points_A[:, 0], points_A[:, 1], points_A[:, 2], c='r', marker='o', label='Set A')
ax.scatter(points_B[:, 0], points_B[:, 1], points_B[:, 2], c='g', marker='^', label='Set B')
ax.scatter(points_C[:, 0], points_C[:, 1], points_C[:, 2], c='b', marker='s', label='Set C')

# Calculate the intersection points
intersection_points = np.array([[x, y, z] for x in A.intersection(B).intersection(C)])

# Plot the intersection points
if len(intersection_points) > 0:
    ax.scatter(intersection_points[:, 0], intersection_points[:, 1], intersection_points[:, 2], c='purple', marker='x', label='Intersection')

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('Inclusion-Exclusion Principle Visualization')
ax.legend()

plt.show()
