import numpy as np
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from IPython.display import display, clear_output
import time

# Parametric curve functions
def x(t):
    return np.cos(t)

def y(t):
    return np.sin(2 * t)

def derivative_x(t):
    return -np.sin(t)

def derivative_y(t):
    return 2 * np.cos(2 * t)

# Create time values for animation
t_values = np.linspace(0, 2 * np.pi, 100)

# Create Plotly figure
fig = make_subplots(rows=1, cols=1, specs=[[{'type': 'scatter'}]])

# Initialize empty scatter plot
scatter = go.Scatter(
    x=[],
    y=[],
    mode='markers+lines',
    marker=dict(
        size=8,
        color=[],
        colorscale='Viridis',
        opacity=0.8
    )
)

fig.add_trace(scatter)
fig.update_layout(title='Creative Animated Parametric Curve')

for t in t_values:
    # Update scatter plot data
    scatter.x = [x(t)]
    scatter.y = [y(t)]
    scatter.marker.color = [t]  # Use time parameter for color gradient
    
    # Update tangent line data
    tangent_x = [x(t), x(t) + derivative_x(t)]
    tangent_y = [y(t), y(t) + derivative_y(t)]
    
    # Update normal line data
    normal_x = [x(t), x(t) - derivative_y(t)]
    normal_y = [y(t), y(t) + derivative_x(t)]
    
    scatter_line = go.Scatter(
        x=tangent_x,
        y=tangent_y,
        mode='lines',
        line=dict(color='red', width=2, dash='dash'),
        showlegend=False
    )
    
    scatter_normal = go.Scatter(
        x=normal_x,
        y=normal_y,
        mode='lines',
        line=dict(color='green', width=2, dash='dash'),
        showlegend=False
    )
    
    # Add annotations for explanation
    annotation_tangent = go.Annotation(
        x=x(t) + derivative_x(t) * 0.6,
        y=y(t) + derivative_y(t) * 0.6,
        xref='x',
        yref='y',
        text='Tangent',
        showarrow=True,
        arrowhead=3
    )
    
    annotation_normal = go.Annotation(
        x=x(t) - derivative_y(t) * 0.6,
        y=y(t) + derivative_x(t) * 0.6,
        xref='x',
        yref='y',
        text='Normal',
        showarrow=True,
        arrowhead=3
    )
    
    fig.add_trace(scatter_line)
    fig.add_trace(scatter_normal)
    fig.add_annotation(annotation_tangent)
    fig.add_annotation(annotation_normal)
    
    # Update layout
    fig.update_xaxes(range=[-1.5, 1.5])
    fig.update_yaxes(range=[-1.5, 1.5])
    
    # Display the figure
    clear_output(wait=True)
    display(fig)
    time.sleep(0.1)

# Save the final frame of the animation
fig.write_html('creative_parametric_animation.html')

# Display the final frame
clear_output(wait=True)
display(fig)
