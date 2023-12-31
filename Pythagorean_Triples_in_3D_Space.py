import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def generate_pythagorean_triples(limit):
    triples = []
    for x in range(1, limit):
        for y in range(x, limit):
            z = np.sqrt(x**2 + y**2)
            if z == int(z):
                triples.append((x, y, int(z)))
    return triples

def plot_pythagorean_triples(triples):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for triple in triples:
        x, y, z = triple
        vertices = [(0, 0, 0), (x, 0, 0), (0, y, 0), (0, 0, z)]
        faces = [[vertices[0], vertices[1], vertices[3]], 
                 [vertices[0], vertices[2], vertices[3]], 
                 [vertices[1], vertices[2], vertices[3]]]
        ax.add_collection3d(Poly3DCollection(faces, linewidths=1, edgecolors='k', alpha=0.2))

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Pythagorean Triples in 3D Space')
    plt.show()

# Generate and plot Pythagorean Triples up to a certain limit
limit = 20
pythagorean_triples = generate_pythagorean_triples(limit)
plot_pythagorean_triples(pythagorean_triples)
