import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Generate matrices for animation
num_frames = 20
initial_matrix = np.array([[4, 3], [2, 1]])
matrices = [initial_matrix + i for i in range(num_frames)]

# Convert matrices to pandas DataFrames
dfs = [pd.DataFrame(mat, columns=['Column 1', 'Column 2']) for mat in matrices]

# Create initial heatmap using plotly
fig = px.imshow(dfs[0], labels=dict(color="Matrix Transformation"), title="Matrix Transformation Animation")

# Build animation
frames = [go.Frame(data=[go.Heatmap(z=df.values, colorscale='Viridis')]) for df in dfs]
fig.frames = frames

# Configure animation layout
fig.update_layout(
    updatemenus=[{
        'type': 'buttons',
        'x': 0.1,
        'y': 0,
        'xanchor': 'right',
        'yanchor': 'top',
        'buttons': [{
            'label': 'Play',
            'method': 'animate',
            'args': [None, {'frame': {'duration': 100, 'redraw': True}, 'fromcurrent': True}],
        }, {
            'label': 'Pause',
            'method': 'animate',
            'args': [[None], {'frame': {'duration': 0, 'redraw': True}, 'mode': 'immediate', 'transition': {'duration': 0}}],
        }],
    }],
)

# Display the animation
fig.show()
