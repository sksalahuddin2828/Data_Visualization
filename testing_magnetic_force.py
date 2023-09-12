import numpy as np
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import sympy as sp
from IPython.display import display, HTML, Math

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
data = {
    'Component': ['X', 'Y', 'Z'],
    'Force (N)': F_vector_np,
    'Velocity (m/s)': v_vector_np,
    'Magnetic Field (T)': B_vector_np,
    'Direction of Force': cross_product_np
}

# Display mathematical expressions
display(Math(r'F = q \cdot v \cdot B'))
display(Math(r'F_{\text{vector}} = ' + sp.latex(F_vector)))
display(Math(r'v_{\text{vector}} = ' + sp.latex(v_vector)))
display(Math(r'B_{\text{vector}} = ' + sp.latex(B_vector)))
display(Math(r'\text{Direction of Force} = ' + sp.latex(cross_product)))

# Create an animation of vector evolution
t_values = np.linspace(0, 1, 20)
animation_frames = []

for t in t_values:
    animated_F_vector_np = t * F_vector_np
    animated_v_vector_np = t * v_vector_np
    animated_B_vector_np = t * B_vector_np
    animated_cross_product_np = t * cross_product_np
    
    animation_frames.append(
        go.Scatter3d(
            x=[0, animated_F_vector_np[0]],
            y=[0, animated_F_vector_np[1]],
            z=[0, animated_F_vector_np[2]],
            name='Magnetic Force',
            line=dict(width=5, color='red')
        )
    )

# Create a 3D plot using Plotly with subplots
fig = make_subplots(
    rows=1, cols=2,
    specs=[[{'type': 'scatter3d'}, {'type': 'table'}]],
    subplot_titles=['Vector Animation', 'Vector Data'],
)

# Add animation frames to the 3D plot
for frame in animation_frames:
    fig.add_trace(frame)

# Add table with vector data
table_trace = go.Table(
    header=dict(values=list(data.keys())),
    cells=dict(values=[data[col] for col in data.keys()])
)
fig.add_trace(table_trace, row=1, col=2)

# Set axis labels
fig.update_layout(scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Z'))

# Set plot limits for better visualization
fig.update_scenes(aspectmode="data", aspectratio=dict(x=1, y=1, z=1))

# Set camera angle and initial position
camera = dict(up=dict(x=0, y=0, z=1), center=dict(x=0, y=0, z=0), eye=dict(x=-1.5, y=-1.5, z=0.5))
fig.update_layout(scene_camera=camera)

# Add a legend
fig.update_layout(legend=dict(x=0.8, y=0.9))

# Set subplot titles
fig.update_layout(title_text="Magnetic Force Visualization")

# Add a creative annotation
fig.add_annotation(
    text="Electromagnetism in Action!",
    x=0.1, y=0.95,
    showarrow=False,
    font=dict(size=16, color='blue'),
    bgcolor='lightyellow',
)

# Add a creative background
fig.update_layout(
    scene=dict(
        xaxis_backgroundcolor='aliceblue',
        yaxis_backgroundcolor='aliceblue',
        zaxis_backgroundcolor='aliceblue',
    )
)

# Show the interactive plot in Jupyter Notebook or export as HTML
fig.show()

# Print the calculated force
print(f"The magnetic force is {F:.2e} N.")
