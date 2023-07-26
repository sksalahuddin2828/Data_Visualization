import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def find_diophantine_solution(k):
    for x in range(-k, k+1):
        for y in range(-k, k+1):
            for z in range(-k, k+1):
                if x**3 + y**3 + z**3 == k:
                    return x, y, z
    return None, None, None

def plot_diophantine_solutions(k_values):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    for k in k_values:
        x, y, z = find_diophantine_solution(k)
        if x is not None:
            ax.scatter(x, y, z, c=[k], marker='o', s=100, cmap='viridis')

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    cbar = plt.colorbar(ax.scatter([], [], [], c=[], cmap='viridis'), ax=ax)
    cbar.set_label('Value of k')

    ax.set_title('Solutions for Diophantine Equation x³ + y³ + z³ = k')

    plt.show()

# Generate a list of k values from 1 to 100
k_values = list(range(1, 101))
plot_diophantine_solutions(k_values)
