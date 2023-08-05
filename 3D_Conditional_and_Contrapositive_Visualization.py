import pandas as pd
import plotly.graph_objects as go

# Example 2: Visualize p → q and its contrapositive ~q → ~p in 3D

fig = go.Figure()

# Plot p → q
fig.add_trace(go.Scatter3d(x=df['p'], y=df['q'], z=df['p → q'], mode='markers', marker=dict(color='blue'), name='p → q'))

# Plot ~q → ~p
fig.add_trace(go.Scatter3d(x=df['p'], y=df['q'], z=df['~q → ~p'], mode='markers', marker=dict(color='red'), name='~q → ~p'))

# Update layout
fig.update_layout(
    scene=dict(
        xaxis_title='p',
        yaxis_title='q',
        zaxis_title='Result',
        annotations=[
            dict(
                showarrow=False,
                x=0.5,
                y=1.1,
                z=0,
                text='Conditional and Contrapositive Visualization',
                xanchor='center',
                font=dict(size=16)
            )
        ]
    ),
    margin=dict(l=0, r=0, b=0, t=0),
)

# Show the interactive plot
fig.show()
