import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import plotly.graph_objects as go

def pareto_principle(vectors, values):
    # Sort the vectors and values together based on values in descending order
    sorted_indices = np.argsort(values)[::-1]
    sorted_vectors = vectors[sorted_indices]
    sorted_values = values[sorted_indices]

    # Calculate the cumulative sum of values
    cumulative_sum = np.cumsum(sorted_values)

    # Calculate the total value
    total_value = cumulative_sum[-1]

    # Find the threshold value that represents 80% of the total value
    threshold = total_value * 0.8

    # Find the index where the cumulative sum exceeds the threshold
    index_80 = np.argmax(cumulative_sum >= threshold)

    # Extract the top 20% of vectors and their corresponding values based on the index
    top_20_vectors = sorted_vectors[:index_80 + 1]
    top_20_values = sorted_values[:index_80 + 1]

    # Calculate the percentage of total value contributed by the top 20% vectors
    percentage_80 = (np.sum(top_20_values) / total_value) * 100

    return top_20_vectors, percentage_80


def create_random_vectors(num_vectors, vector_length):
    # Generate random vectors and random values for demonstration
    vectors = np.random.rand(num_vectors, vector_length)  # Random vectors
    values = np.random.randint(100, 1000, size=num_vectors)  # Random values for vectors
    return vectors, values


def visualize_vectors(vectors, values, percentage_80=None):
    # Convert the vectors and values to a pandas DataFrame for easier manipulation
    df = pd.DataFrame({'X': vectors[:, 0], 'Y': vectors[:, 1], 'Z': vectors[:, 2], 'Value': values})

    # Create a 3D scatter plot using Plotly
    fig = go.Figure(data=[go.Scatter3d(x=df['X'], y=df['Y'], z=df['Z'], mode='markers',
                                       marker=dict(size=6, color=df['Value'], colorscale='Viridis', opacity=0.8))])

    if percentage_80 is not None:
        # Highlight the top 20% vectors with a different color and larger markers
        top_20_indices = np.arange(len(vectors))[:len(vectors) * 20 // 100]
        fig.add_trace(go.Scatter3d(x=df['X'][top_20_indices], y=df['Y'][top_20_indices], z=df['Z'][top_20_indices], mode='markers',
                                   marker=dict(size=10, color='red', opacity=1)))

        # Set axis labels and title
        fig.update_layout(scene=dict(xaxis_title='Function 1', yaxis_title='Function 2', zaxis_title='Function 3'),
                          title='Pareto Principle for Random Vectors', showlegend=False)

        # Add annotation to show the percentage of total value contributed by top 20% vectors
        annotation_text = f"Top 20% Vectors: {percentage_80:.2f}% of Total Value"
        fig.add_annotation(dict(x=0.1, y=0.9, xref="paper", yref="paper", text=annotation_text,
                                showarrow=False, font=dict(size=12)))

    # Show the interactive 3D scatter plot
    fig.show()


def main():
    # Generate random vectors with 100 vectors, each having 3 dimensions
    num_vectors = 100
    vector_length = 3
    vectors, values = create_random_vectors(num_vectors, vector_length)

    # Visualize the vectors using an interactive 3D scatter plot with Plotly
    visualize_vectors(vectors, values)

    # Apply the Pareto Principle and get the top 20% vectors and their contribution percentage
    top_20_vectors, percentage_80 = pareto_principle(vectors, values)

    # Visualize the top 20% vectors using a 3D scatter plot with Matplotlib
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(top_20_vectors[:, 0], top_20_vectors[:, 1], top_20_vectors[:, 2], s=100, c='red', label='Top 20% Vectors')
    ax.set_xlabel('Function 1')
    ax.set_ylabel('Function 2')
    ax.set_zlabel('Function 3')
    ax.set_title('Top 20% Vectors using Pareto Principle (Matplotlib)')
    ax.legend()
    plt.show()

if __name__ == '__main__':
    main()
