import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Generate a skew-symmetric matrix
def generate_skew_symmetric_matrix(size):
    mat = np.random.rand(size, size)
    skew_symmetric = (mat - mat.T) / 2
    return skew_symmetric

# Create an animated scatter plot with enhanced features
def animate_scatter_plot(matrix):
    fig = make_subplots(rows=1, cols=2, specs=[[{'type': 'scatter3d'}, {'type': 'scatter'}]],
                        subplot_titles=("Matrix Evolution", "Heatmap"))

    frames = []

    size = matrix.shape[0]

    for i in range(size):
        frame_data = matrix[:i+1, :i+1]
        x, y = np.meshgrid(np.arange(i+1), np.arange(i+1))
        x = x.flatten()
        y = y.flatten()
        z = frame_data.flatten()

        scatter_trace = go.Scatter3d(x=x, y=y, z=z, mode='markers',
                                     marker=dict(size=10, color=z, colorscale='Viridis'))
        fig.add_trace(scatter_trace, row=1, col=1)

        heatmap_trace = go.Heatmap(z=frame_data, colorscale='Jet')
        fig.add_trace(heatmap_trace, row=1, col=2)

        frames.append(go.Frame(data=[scatter_trace, heatmap_trace], name=f'Frame {i + 1}'))

    animation_fig = go.Figure(fig, frames=frames)

    animation_fig.update_layout(
        updatemenus=[{
            "buttons": [
                {
                    "args": [None, {"frame": {"duration": 500, "redraw": True}, "fromcurrent": True}],
                    "label": "Play",
                    "method": "animate",
                },
                {
                    "args": [[None], {"frame": {"duration": 0, "redraw": True}, "mode": "immediate", "transition": {"duration": 0}}],
                    "label": "Pause",
                    "method": "animate",
                },
            ],
            "direction": "left",
            "pad": {"r": 10, "t": 87},
            "showactive": False,
            "type": "buttons",
            "x": 0.1,
            "xanchor": "right",
            "y": 0,
            "yanchor": "top",
        }],
        sliders=[{
            "active": 0,
            "steps": [{
                "args": [[f.name], {"frame": {"duration": 300, "redraw": True}, "transition": {"duration": 0}}],
                "label": f"Frame {i + 1}",
                "method": "animate",
            } for i, f in enumerate(animation_fig.frames)],
            "x": 0.1,
            "xanchor": "left",
            "y": 0,
            "yanchor": "top",
            "currentvalue": {
                "font": {"size": 20},
                "prefix": "Frame:",
                "visible": True,
                "xanchor": "right",
            },
        }]
    )

    animation_fig.update_yaxes(showticklabels=False, showgrid=False)
    animation_fig.update_xaxes(showticklabels=False, showgrid=False)
    animation_fig.update_layout(title_text='Skew-Symmetric Matrix Animation')

    return animation_fig

# Example usage
size = 7
matrix = generate_skew_symmetric_matrix(size)
animation_fig = animate_scatter_plot(matrix)
animation_fig.show()
