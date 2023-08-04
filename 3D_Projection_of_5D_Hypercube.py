import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def generate_hypercube_vertices():
    vertices = []
    for i in range(2):
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    for m in range(2):
                        vertices.append([i, j, k, l, m])
    return vertices

def generate_hypercube_edges(vertices):
    edges = []
    for i in range(len(vertices)):
        for j in range(i+1, len(vertices)):
            dist = np.sum(np.array(vertices[i]) != np.array(vertices[j]))
            if dist == 1:
                edges.append([vertices[i], vertices[j]])
    return edges

def project_to_3d(vertices):
    return [vertex[:3] for vertex in vertices]

def visualize_hypercube(vertices, edges):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for edge in edges:
        points = np.array(edge)
        ax.plot3D(points[:, 0], points[:, 1], points[:, 2], 'b')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D Projection of 5D Hypercube')

    plt.show()

def main():
    vertices = generate_hypercube_vertices()
    edges = generate_hypercube_edges(vertices)
    vertices_3d = project_to_3d(vertices)
    visualize_hypercube(vertices_3d, edges)

if __name__ == "__main__":
    main()
