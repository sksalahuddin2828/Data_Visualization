import pandas as pd
import plotly.graph_objects as go
import numpy as np

# Generate synthetic bacteria movement data
np.random.seed(42)
n_samples = 100
x_coordinates = np.random.uniform(-10, 10, n_samples)
y_coordinates = np.random.uniform(-10, 10, n_samples)
direction_angles = np.random.uniform(0, 2 * np.pi, n_samples)

data = pd.DataFrame({
    'X Coordinate': x_coordinates,
    'Y Coordinate': y_coordinates,
    'Direction Angle': direction_angles
})

# Function to perform rotation transformation on movement vectors
def rotate_vector(x, y, angle):
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                [np.sin(angle), np.cos(angle)]])
    vector = np.array([x, y])
    return np.dot(rotation_matrix, vector)

# Function to perform scaling transformation on movement vectors
def scale_vector(x, y, scaling_factor):
    return x * scaling_factor, y * scaling_factor

# Apply rotation transformation on the movement vectors
data['Rotated_X'], data['Rotated_Y'] = zip(*data.apply(lambda row: rotate_vector(row['X Coordinate'],
                                                                                 row['Y Coordinate'],
                                                                                 row['Direction Angle']), axis=1))

# Apply scaling transformation on the movement vectors
scaling_factor = 2.0
data['Scaled_X'], data['Scaled_Y'] = zip(*data.apply(lambda row: scale_vector(row['X Coordinate'],
                                                                             row['Y Coordinate'],
                                                                             scaling_factor), axis=1))

# Create a 2D vector plot to visualize the transformations
fig = go.Figure()

# Original vectors
fig.add_trace(go.Scatter(x=data['X Coordinate'], y=data['Y Coordinate'],
                         mode='markers', name='Original Position', marker=dict(size=10)))

# Rotated vectors after linear transformation
fig.add_trace(go.Scatter(x=data['Rotated_X'], y=data['Rotated_Y'],
                         mode='markers', name='Rotated Position', marker=dict(size=10)))

# Scaled vectors after linear transformation
fig.add_trace(go.Scatter(x=data['Scaled_X'], y=data['Scaled_Y'],
                         mode='markers', name='Scaled Position', marker=dict(size=10)))

# Add vector arrows
for _, row in data.iterrows():
    fig.add_trace(go.Scatter(x=[row['X Coordinate'], row['Rotated_X']],
                             y=[row['Y Coordinate'], row['Rotated_Y']],
                             mode='lines', showlegend=False, line=dict(color='gray')))
    fig.add_trace(go.Scatter(x=[row['X Coordinate'], row['Scaled_X']],
                             y=[row['Y Coordinate'], row['Scaled_Y']],
                             mode='lines', showlegend=False, line=dict(color='gray')))

fig.update_layout(title='Bacteria Movement - Linear Transformations',
                  xaxis_title='X Coordinate', yaxis_title='Y Coordinate',
                  template='plotly_dark')

fig.show()
