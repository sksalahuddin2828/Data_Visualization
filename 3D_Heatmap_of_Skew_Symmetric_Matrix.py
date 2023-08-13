import numpy as np
import pandas as pd
import plotly.express as px

# Generate a skew-symmetric matrix
def generate_skew_symmetric_matrix(size):
    mat = np.random.rand(size, size)
    skew_symmetric = (mat - mat.T) / 2
    return skew_symmetric

# Verify if a matrix is skew-symmetric
def is_skew_symmetric(matrix):
    return np.allclose(matrix, -matrix.T)

# Create an interactive heatmap using Plotly
def plot_heatmap(matrix):
    df = pd.DataFrame(matrix)
    fig = px.imshow(df,
                    labels=dict(x="Column", y="Row", color="Value"),
                    title="Heatmap of Skew-Symmetric Matrix",
                    color_continuous_scale="Viridis")
    fig.update_xaxes(side="top")
    fig.update_layout(xaxis_title="Column", yaxis_title="Row")
    fig.show()

# Example usage
size = 5
matrix = generate_skew_symmetric_matrix(size)
print("Generated Matrix:")
print(matrix)
print("Is Skew-Symmetric:", is_skew_symmetric(matrix))

plot_heatmap(matrix)
