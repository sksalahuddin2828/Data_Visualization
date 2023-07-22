import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def euler_identity(x):
    # Euler's Identity: e^(iπ) + 1 = 0
    return np.exp(1j * x) + 1

def euler_formula_for_cube(vertices, edges, faces):
    # Euler's formula for a cube: V - E + F = 2
    return vertices - edges + faces

def plot_cube():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Define the vertices, edges, and faces of a cube
    vertices = np.array([[1, 1, 1], [1, -1, 1], [1, -1, -1], [1, 1, -1],
                         [-1, 1, 1], [-1, -1, 1], [-1, -1, -1], [-1, 1, -1]])
    edges = [[0, 1], [1, 2], [2, 3], [3, 0], [4, 5], [5, 6], [6, 7], [7, 4],
             [0, 4], [1, 5], [2, 6], [3, 7]]
    faces = [[0, 1, 2, 3], [3, 2, 6, 7], [7, 6, 5, 4], [4, 5, 1, 0],
             [5, 6, 2, 1], [7, 4, 0, 3]]

    # Plot the cube
    ax.add_collection3d(Poly3DCollection([vertices[face] for face in faces], facecolors='cyan', linewidths=1, edgecolors='r', alpha=0.6))

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D Visualization of a Cube')

    plt.show()

if __name__ == "__main__":
    # Example 1: Euler's Identity
    x = np.pi
    euler_result = euler_identity(x)
    print(f"Euler's Identity: e^(iπ) + 1 = {euler_result}")

    # Example 2: Euler's formula for a cube
    vertices = 8
    edges = 12
    faces = 6
    euler_formula_result = euler_formula_for_cube(vertices, edges, faces)
    print(f"Euler's formula for a cube: {vertices} - {edges} + {faces} = {euler_formula_result}")

    # Example 3: 3D Visualization of a Cube
    plot_cube()
