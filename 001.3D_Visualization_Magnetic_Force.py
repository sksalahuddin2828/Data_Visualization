import numpy as np
import plotly.graph_objs as go
import pandas as pd
import sympy as sp

# Given data
q = 20e-9  # Charge in Coulombs
v = 10.0  # Velocity in m/s
B = 5e-5  # Magnetic field strength in Tesla

# Calculate the magnetic force
F = q * v * B

# Create a symbolic variable for the force vector
F_vector = sp.Matrix([0, 0, -F])

# Create a symbolic variable for the velocity vector
v_vector = sp.Matrix([v, 0, 0])

# Create a symbolic variable for the magnetic field vector
B_vector = sp.Matrix([0, 0, B])

# Calculate the cross product of v and B to find the direction of the force
cross_product = v_vector.cross(B_vector)

# Convert SymPy matrices to NumPy arrays for plotting
F_vector_np = np.array(F_vector).astype(float).flatten()
v_vector_np = np.array(v_vector).astype(float).flatten()
B_vector_np = np.array(B_vector).astype(float).flatten()
cross_product_np = np.array(cross_product).astype(float).flatten()

# Create a Pandas DataFrame to store vector data
data = pd.DataFrame({
    'Component': ['X', 'Y', 'Z'],
    'Force': F_vector_np,
    'Velocity': v_vector_np,
    'Magnetic Field': B_vector_np,
    'Direction of Force': cross_product_np
})

# Create a 3D plot using Plotly
fig = go.Figure(data=[
    go.Scatter3d(x=[0, F_vector_np[0]], y=[0, F_vector_np[1]], z=[0, F_vector_np[2]], name='Magnetic Force', line=dict(width=5, color='red')),
    go.Scatter3d(x=[0, v_vector_np[0]], y=[0, v_vector_np[1]], z=[0, v_vector_np[2]], name='Velocity', line=dict(width=5, color='blue')),
    go.Scatter3d(x=[0, B_vector_np[0]], y=[0, B_vector_np[1]], z=[0, B_vector_np[2]], name='Magnetic Field', line=dict(width=5, color='green')),
    go.Scatter3d(x=[0, cross_product_np[0]], y=[0, cross_product_np[1]], z=[0, cross_product_np[2]], name='Direction of Force', line=dict(width=5, color='black'))
])

# Set axis labels
fig.update_layout(scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Z'))

# Set plot limits for better visualization
fig.update_scenes(aspectmode="data", aspectratio=dict(x=1, y=1, z=1))

# Set camera angle and initial position
camera = dict(up=dict(x=0, y=0, z=1), center=dict(x=0, y=0, z=0), eye=dict(x=-1.5, y=-1.5, z=0.5))
fig.update_layout(scene_camera=camera)

# Add a legend
fig.update_layout(legend=dict(x=0.8, y=0.9))

# Show the interactive plot in Jupyter Notebook or export as HTML
fig.show()

# Print the calculated force
print(f"The magnetic force is {F:.2e} N.")
