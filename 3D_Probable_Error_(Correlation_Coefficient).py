import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Function to calculate probable error
def probable_error(r, N):
    return 0.674 * (1 - r**2) / np.sqrt(N)

# Generate sample data using Pandas
np.random.seed(42)
num_samples = 100
data = pd.DataFrame({
    'Sample': range(1, num_samples + 1),
    'Correlation Coefficient': np.random.uniform(-1, 1, num_samples),
    'Sample Size': np.random.randint(2, 101, num_samples)
})

# Calculate Probable Error using the provided formula
data['Probable Error'] = probable_error(data['Correlation Coefficient'], data['Sample Size'])

# Create a 3D scatter plot
fig = make_subplots(rows=1, cols=1, specs=[[{'type': 'scatter3d'}]])
scatter = go.Scatter3d(
    x=data['Correlation Coefficient'],
    y=data['Sample Size'],
    z=data['Probable Error'],
    mode='markers',
    marker=dict(
        size=8,
        color=data['Probable Error'],  # Color points based on Probable Error
        colorscale='Viridis',  # Choose a color scale
        colorbar=dict(title='Probable Error'),  # Add color bar with a title
        opacity=0.7,
    )
)
fig.add_trace(scatter)

# Update layout for better aesthetics and interactivity
fig.update_layout(
    title='Probable Error for Correlation Coefficient',
    scene=dict(
        xaxis_title='Correlation Coefficient (r)',
        yaxis_title='Sample Size (N)',
        zaxis_title='Probable Error',
    ),
    scene_camera=dict(up=dict(x=0, y=0, z=1), eye=dict(x=1.25, y=1.25, z=1.25)),
)

# Show the interactive plot
fig.show()
