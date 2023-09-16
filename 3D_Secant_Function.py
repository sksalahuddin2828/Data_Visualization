import numpy as np
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

# Step 1: Generate a range of angles
angles = np.linspace(0.01, np.pi / 2, 100)  # 100 angles from 0.01 to π/2

# Step 2: Calculate Secant Values using NumPy
sec_values = 1 / np.cos(angles)

# Create a DataFrame
data = pd.DataFrame({'Angle': angles, 'Secant': sec_values})

# Step 3: Data Visualization using Plotly
fig = go.Figure()

# Add a 3D line trace
fig.add_trace(
    go.Scatter3d(
        x=data['Angle'],
        y=data['Secant'],
        z=data['Secant'],
        mode='lines',
        name='sec(θ)'
    )
)

# Customize the plot
fig.update_layout(
    scene=dict(
        xaxis_title='θ',
        yaxis_title='sec(θ)',
        zaxis_title='sec(θ)',
    ),
    title='Secant Function',
)

# Show the interactive plot
fig.show()
