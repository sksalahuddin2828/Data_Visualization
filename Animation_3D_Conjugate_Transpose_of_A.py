import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def animate_plotly_3d_matrix(matrix, title):
    size = matrix.shape[0]
    fig = make_subplots(rows=1, cols=1, specs=[[{'type': 'scatter3d'}]])
    
    frames = [go.Frame(data=[go.Scatter3d(x=np.arange(i+1).flatten(),
                                          y=np.arange(i+1).flatten(),
                                          z=np.real(matrix[:i+1, :i+1]).flatten(),
                                          mode='markers',
                                          marker=dict(size=10, color=np.real(matrix[:i+1, :i+1]).flatten(),
                                                      colorscale='Viridis'))],
                        name=f'Frame {i+1}') for i in range(size)]
    
    scatter_trace = go.Scatter3d(x=[],
                                 y=[],
                                 z=[],
                                 mode='markers',
                                 marker=dict(size=10, color=[],
                                             colorscale='Viridis'))
    
    fig.add_trace(scatter_trace)
    fig.update_layout(updatemenus=[dict(type="buttons", showactive=False, buttons=[dict(label="Play",
                                                                                            method="animate",
                                                                                            args=[None, {"frame": {"duration": 500, "redraw": True},
                                                                                                         "fromcurrent": True}]),
                                                                                  dict(label="Pause",
                                                                                       method="animate",
                                                                                       args=[[None], {"frame": {"duration": 0, "redraw": True},
                                                                                                      "mode": "immediate",
                                                                                                      "transition": {"duration": 0}}])])])
    
    fig.frames = frames
    
    fig.update_layout(title=title)
    fig.update_layout(scene=dict(aspectmode='data'))
    animation = go.Figure(fig)

    animation.show()

# Call the function for different matrices
animate_plotly_3d_matrix(A, 'Matrix A')
