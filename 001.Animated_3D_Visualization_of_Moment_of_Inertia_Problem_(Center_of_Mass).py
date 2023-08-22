import numpy as np
import sympy as sp
import plotly.express as px
import pandas as pd

# Define symbols
m, R, d = sp.symbols('m R d')

# Define equation
equation = sp.Eq(m * d**2, (13 * m * R**2))

# Solve the equation
solution = sp.solve(equation, d)

# Convert solution to a numerical function
R_value = 1.0  # Assign a value to R
solution_func = sp.lambdify(R, solution[0], 'numpy')
solution_value = solution_func(R_value)

# Create a grid of points for visualization
grid_size = 20
x_vals = np.linspace(-R_value, R_value, grid_size)
y_vals = np.linspace(-R_value, R_value, grid_size)
x_grid, y_grid = np.meshgrid(x_vals, y_vals)
z_grid = np.zeros_like(x_grid)

# Create a list of DataFrames for animation frames
frames_data = []
for frame_num in range(grid_size):
    frame = pd.DataFrame({
        'x': [0, solution_value],
        'y': [0, 0],
        'z': [0, 0]
    })
    frame['x_obj'] = x_vals[frame_num]
    frames_data.append(frame)

# Create the animated scatter plot using Plotly Express
fig = px.scatter_3d(
    frames_data[0],
    x='x',
    y='y',
    z='z',
    text=["Center of Mass", "Object Position"],
    labels={'x': 'X-axis', 'y': 'Y-axis', 'z': 'Z-axis'},
    animation_frame='x_obj',
    title="Animated 3D Visualization of Moment of Inertia Problem"
)

# Add a surface representing the object's position
fig.add_surface(
    x=x_grid,
    y=y_grid,
    z=z_grid,
    colorscale='Viridis',
    showscale=False,
    opacity=0.7
)

# Customize the scene to add a line connecting the points
fig.update_layout(
    scene=dict(
        aspectmode="cube",
        camera=dict(eye=dict(x=-1, y=-1, z=1.5))
    )
)

# Show the interactive animated plot
fig.show()
