import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Example ordered triple
ordered_triple = [(1, 2, 3), (2, 3, 4), (3, 4, 5), (4, 5, 6)]

# Create a DataFrame from the ordered triple
df = pd.DataFrame(ordered_triple, columns=['X', 'Y', 'Z'])

# Create an animated 3D scatter plot
fig = go.Figure()

for i in range(len(df)):
    # Scatter plot for each ordered triple
    fig.add_trace(go.Scatter3d(
        x=[df['X'][i]], y=[df['Y'][i]], z=[df['Z'][i]],
        mode='markers',
        marker=dict(size=8, color='red', opacity=0.8),
        name=f'Triple {i+1}',
    ))

# Set layout for the 3D scatter plot
fig.update_layout(
    title_text='Mathematical Dance of Ordered Triples',
    scene=dict(
        xaxis=dict(title='X-axis'),
        yaxis=dict(title='Y-axis'),
        zaxis=dict(title='Z-axis'),
    ),
    scene_camera=dict(
        eye=dict(x=0.8, y=-1.2, z=0.5),
        up=dict(x=0, y=0, z=1),
    ),
    hovermode='closest',
    showlegend=True,
)

# Add animation slider
steps = []
for i in range(len(df)):
    step = dict(
        method='update',
        args=[{'visible': [False] * len(df)},
              {'title': f'Triple {i+1}'}],
    )
    step['args'][0]['visible'][i] = True
    steps.append(step)

sliders = [dict(
    active=0,
    steps=steps,
)]

# Add sliders to the layout
fig.update_layout(
    sliders=sliders,
)

# Show the animated 3D scatter plot
fig.show()
