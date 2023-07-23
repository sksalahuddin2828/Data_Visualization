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
    'Correlation Coefficient': np.random.uniform(-1, 1, num_samples),
    'Sample Size': np.random.randint(2, 101, num_samples)
})

# Calculate Probable Error using the provided formula
data['Probable Error'] = probable_error(data['Correlation Coefficient'], data['Sample Size'])

# Create a grid of correlation coefficient and sample size values
r_values = np.linspace(-1, 1, 100)
N_values = np.linspace(2, 100, 100)
R, N = np.meshgrid(r_values, N_values)

# Calculate the Probable Error for the entire grid using the formula
probable_error_grid = probable_error(R, N)

# Apply a mathematical transformation to make the surface more interesting
transformed_probable_error = probable_error_grid * (1 + np.sin(N) * np.cos(R * np.pi))

# Create a 3D surface plot
fig = make_subplots(rows=1, cols=1, specs=[[{'type': 'surface'}]])
surface = go.Surface(
    x=r_values,
    y=N_values,
    z=transformed_probable_error,
    colorscale='Viridis',  # Choose a color scale
    colorbar=dict(title='Probable Error'),  # Add color bar with a title
    showscale=True,
)
fig.add_trace(surface)

# Update layout for better aesthetics and interactivity
fig.update_layout(
    title='Probable Error for Correlation Coefficient and Sample Size',
    scene=dict(
        xaxis_title='Correlation Coefficient (r)',
        yaxis_title='Sample Size (N)',
        zaxis_title='Probable Error',
    ),
    scene_camera=dict(up=dict(x=0, y=0, z=1), eye=dict(x=1.25, y=1.25, z=1.25)),
)

# Show the interactive plot
fig.show()
