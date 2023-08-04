import pandas as pd
import plotly.graph_objects as go
import numpy as np

# Generate synthetic bacteria movement data in 5D
np.random.seed(42)
n_samples = 100
x_coordinates = np.random.uniform(-10, 10, n_samples)
y_coordinates = np.random.uniform(-10, 10, n_samples)
z_coordinates = np.random.uniform(-5, 5, n_samples)
velocity = np.random.uniform(1, 5, n_samples)
acceleration = np.random.uniform(0.5, 2, n_samples)
direction_angles_x = np.random.uniform(0, 2 * np.pi, n_samples)
direction_angles_y = np.random.uniform(0, 2 * np.pi, n_samples)

data_5d = pd.DataFrame({
    'X Coordinate': x_coordinates,
    'Y Coordinate': y_coordinates,
    'Z Coordinate': z_coordinates,
    'Velocity': velocity,
    'Acceleration': acceleration,
    'Direction Angle X': direction_angles_x,
    'Direction Angle Y': direction_angles_y
})

# Function to perform 5D rotation transformation on movement vectors
def rotate_vector_5d(x, y, z, v, a, angle_x, angle_y):
    # For this example, we'll apply rotation to the first 3 dimensions (X, Y, Z)
    rotation_matrix_x = np.array([[1, 0, 0],
                                  [0, np.cos(angle_x), -np.sin(angle_x)],
                                  [0, np.sin(angle_x), np.cos(angle_x)]])
    rotation_matrix_y = np.array([[np.cos(angle_y), 0, np.sin(angle_y)],
                                  [0, 1, 0],
                                  [-np.sin(angle_y), 0, np.cos(angle_y)]])
    vector = np.array([x, y, z])
    rotated_vector = np.dot(rotation_matrix_x, vector)
    rotated_vector = np.dot(rotation_matrix_y, rotated_vector)
    return rotated_vector[0], rotated_vector[1], rotated_vector[2], v, a

# Function to perform 5D scaling transformation on movement vectors
def scale_vector_5d(x, y, z, v, a, scaling_factor):
    return x * scaling_factor, y * scaling_factor, z * scaling_factor, v, a

# Apply 5D rotation transformation on the movement vectors
data_5d['Rotated_X'], data_5d['Rotated_Y'], data_5d['Rotated_Z'], data_5d['Velocity'], data_5d['Acceleration'] = zip(*data_5d.apply(lambda row:
    rotate_vector_5d(row['X Coordinate'], row['Y Coordinate'], row['Z Coordinate'],
                     row['Velocity'], row['Acceleration'], row['Direction Angle X'], row['Direction Angle Y']), axis=1))

# Apply 5D scaling transformation on the movement vectors
scaling_factor_5d = 1.5
data_5d['Scaled_X'], data_5d['Scaled_Y'], data_5d['Scaled_Z'], data_5d['Velocity'], data_5d['Acceleration'] = zip(*data_5d.apply(lambda row:
    scale_vector_5d(row['X Coordinate'], row['Y Coordinate'], row['Z Coordinate'],
                    row['Velocity'], row['Acceleration'], scaling_factor_5d), axis=1))

# Create a 5D vector plot to visualize the transformations
fig = go.Figure()

# Original vectors
fig.add_trace(go.Scatter3d(x=data_5d['X Coordinate'], y=data_5d['Y Coordinate'],
                           z=data_5d['Z Coordinate'], customdata=[data_5d['Velocity'], data_5d['Acceleration']],
                           mode='markers', name='Original Position', marker=dict(size=5)))

# Rotated vectors after linear transformation
fig.add_trace(go.Scatter3d(x=data_5d['Rotated_X'], y=data_5d['Rotated_Y'],
                           z=data_5d['Rotated_Z'], customdata=[data_5d['Velocity'], data_5d['Acceleration']],
                           mode='markers', name='Rotated Position', marker=dict(size=5)))

# Scaled vectors after linear transformation
fig.add_trace(go.Scatter3d(x=data_5d['Scaled_X'], y=data_5d['Scaled_Y'],
                           z=data_5d['Scaled_Z'], customdata=[data_5d['Velocity'], data_5d['Acceleration']],
                           mode='markers', name='Scaled Position', marker=dict(size=5)))

# Add vector arrows
for _, row in data_5d.iterrows():
    fig.add_trace(go.Scatter3d(x=[row['X Coordinate'], row['Rotated_X']],
                               y=[row['Y Coordinate'], row['Rotated_Y']],
                               z=[row['Z Coordinate'], row['Rotated_Z']],
                               customdata=[row['Velocity'], row['Velocity'], row['Acceleration'], row['Acceleration']],
                               mode='lines', showlegend=False, line=dict(color='gray')))
    fig.add_trace(go.Scatter3d(x=[row['X Coordinate'], row['Scaled_X']],
                               y=[row['Y Coordinate'], row['Scaled_Y']],
                               z=[row['Z Coordinate'], row['Scaled_Z']],
                               customdata=[row['Velocity'], row['Velocity'], row['Acceleration'], row['Acceleration']],
                               mode='lines', showlegend=False, line=dict(color='gray')))

fig.update_layout(title='Bacteria Movement - 5D Linear Transformations',
                  scene=dict(xaxis_title='X Coordinate', yaxis_title='Y Coordinate',
                             zaxis_title='Z Coordinate'),
                  template='plotly_dark')

fig.show()
