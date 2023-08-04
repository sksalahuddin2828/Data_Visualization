import pandas as pd
import plotly.graph_objects as go
import numpy as np

# Generate synthetic bacteria movement data in 4D
np.random.seed(42)
n_samples = 100
x_coordinates = np.random.uniform(-10, 10, n_samples)
y_coordinates = np.random.uniform(-10, 10, n_samples)
z_coordinates = np.random.uniform(-5, 5, n_samples)
velocity = np.random.uniform(1, 5, n_samples)
direction_angles_x = np.random.uniform(0, 2 * np.pi, n_samples)
direction_angles_y = np.random.uniform(0, 2 * np.pi, n_samples)

data_4d = pd.DataFrame({
    'X Coordinate': x_coordinates,
    'Y Coordinate': y_coordinates,
    'Z Coordinate': z_coordinates,
    'Velocity': velocity,
    'Direction Angle X': direction_angles_x,
    'Direction Angle Y': direction_angles_y
})

# Function to perform 4D rotation transformation on movement vectors
def rotate_vector_4d(x, y, z, v, angle_x, angle_y):
    rotation_matrix_x = np.array([[1, 0, 0],
                                  [0, np.cos(angle_x), -np.sin(angle_x)],
                                  [0, np.sin(angle_x), np.cos(angle_x)]])
    rotation_matrix_y = np.array([[np.cos(angle_y), 0, np.sin(angle_y)],
                                  [0, 1, 0],
                                  [-np.sin(angle_y), 0, np.cos(angle_y)]])
    vector = np.array([x, y, z])
    rotated_vector = np.dot(rotation_matrix_x, vector)
    rotated_vector = np.dot(rotation_matrix_y, rotated_vector)
    return rotated_vector[0], rotated_vector[1], rotated_vector[2], v

# Function to perform 4D scaling transformation on movement vectors
def scale_vector_4d(x, y, z, v, scaling_factor):
    return x * scaling_factor, y * scaling_factor, z * scaling_factor, v

# Apply 4D rotation transformation on the movement vectors
data_4d['Rotated_X'], data_4d['Rotated_Y'], data_4d['Rotated_Z'], data_4d['Velocity'] = zip(*data_4d.apply(lambda row:
    rotate_vector_4d(row['X Coordinate'], row['Y Coordinate'], row['Z Coordinate'],
                     row['Velocity'], row['Direction Angle X'], row['Direction Angle Y']), axis=1))

# Apply 4D scaling transformation on the movement vectors
scaling_factor_4d = 1.5
data_4d['Scaled_X'], data_4d['Scaled_Y'], data_4d['Scaled_Z'], data_4d['Velocity'] = zip(*data_4d.apply(lambda row:
    scale_vector_4d(row['X Coordinate'], row['Y Coordinate'], row['Z Coordinate'],
                    row['Velocity'], scaling_factor_4d), axis=1))

# Create a 4D vector plot to visualize the transformations
fig = go.Figure()

# Original vectors
fig.add_trace(go.Scatter3d(x=data_4d['X Coordinate'], y=data_4d['Y Coordinate'],
                           z=data_4d['Z Coordinate'], customdata=data_4d['Velocity'],
                           mode='markers', name='Original Position', marker=dict(size=5)))

# Rotated vectors after linear transformation
fig.add_trace(go.Scatter3d(x=data_4d['Rotated_X'], y=data_4d['Rotated_Y'],
                           z=data_4d['Rotated_Z'], customdata=data_4d['Velocity'],
                           mode='markers', name='Rotated Position', marker=dict(size=5)))

# Scaled vectors after linear transformation
fig.add_trace(go.Scatter3d(x=data_4d['Scaled_X'], y=data_4d['Scaled_Y'],
                           z=data_4d['Scaled_Z'], customdata=data_4d['Velocity'],
                           mode='markers', name='Scaled Position', marker=dict(size=5)))

# Add vector arrows
for _, row in data_4d.iterrows():
    fig.add_trace(go.Scatter3d(x=[row['X Coordinate'], row['Rotated_X']],
                               y=[row['Y Coordinate'], row['Rotated_Y']],
                               z=[row['Z Coordinate'], row['Rotated_Z']],
                               customdata=[row['Velocity'], row['Velocity']],
                               mode='lines', showlegend=False, line=dict(color='gray')))
    fig.add_trace(go.Scatter3d(x=[row['X Coordinate'], row['Scaled_X']],
                               y=[row['Y Coordinate'], row['Scaled_Y']],
                               z=[row['Z Coordinate'], row['Scaled_Z']],
                               customdata=[row['Velocity'], row['Velocity']],
                               mode='lines', showlegend=False, line=dict(color='gray')))

fig.update_layout(title='Bacteria Movement - 4D Linear Transformations',
                  scene=dict(xaxis_title='X Coordinate', yaxis_title='Y Coordinate',
                             zaxis_title='Z Coordinate'),
                  template='plotly_dark')

fig.show()
