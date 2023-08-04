import numpy as np
import plotly.graph_objects as go

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

def hardest_logarithm(x, y):
    return np.log(np.abs(x) + np.abs(y))

def visualize_hypercube(vertices, edges):
    fig = go.Figure()

    # Plot 3D surface of the hardest logarithm function
    x = y = np.linspace(-10, 10, 100)
    X, Y = np.meshgrid(x, y)
    Z = hardest_logarithm(X, Y)
    fig.add_trace(go.Surface(x=X, y=Y, z=Z, colorscale='Viridis', name='Hardest Logarithm'))

    for edge in edges:
        points = np.array(edge)
        x, y, z = points[:, 0], points[:, 1], points[:, 2]
        fig.add_trace(go.Scatter3d(x=x, y=y, z=z, mode='lines', line=dict(color='blue'), name='Hypercube Edge'))

    fig.update_layout(scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Z'),
                      title='Creative 3D Visualization of 5D Hypercube with Hardest Logarithm',
                      showlegend=True,
                      width=800, height=800)  # Set width and height here

    fig.show()

def main():
    vertices = generate_hypercube_vertices()
    edges = generate_hypercube_edges(vertices)
    vertices_3d = project_to_3d(vertices)
    visualize_hypercube(vertices_3d, edges)

if __name__ == "__main__":
    main()
