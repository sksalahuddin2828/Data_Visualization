import numpy as np
import plotly.graph_objects as go

# Define the function to be visualized
def complex_function(x_val, a_val):
    return np.exp(-a_val) * np.sin(x_val) * np.sqrt(a_val**2 + x_val**2)

# Create x and a values
x_vals = np.linspace(0, 5, 100)
a_vals = np.linspace(0.1, 5, 50)

# Create meshgrid
X, A = np.meshgrid(x_vals, a_vals)
Z = complex_function(X, A)

# Create an animated 3D surface plot with rotation, pulsation, and color change
fig = go.Figure()

frames = []

for a_val in a_vals:
    y_vals = complex_function(x_vals, a_val)
    color_scale = np.log10(np.abs(y_vals) + 1)
    marker_size = 20 * np.abs(y_vals) / np.max(np.abs(y_vals))
    
    scatter_trace = go.Scatter3d(x=x_vals, y=[a_val] * len(x_vals), z=y_vals,
                                 mode='markers', marker=dict(size=marker_size, color=color_scale, opacity=0.7),
                                 text=[f'x = {x:.2f}<br>a = {a_val:.2f}<br>Value = {y:.2f}' for x, y in zip(x_vals, y_vals)],
                                 hoverinfo='text')
    
    frame_data = [go.Surface(z=Z, x=X, y=A, colorscale='Viridis', cmin=np.min(Z), cmax=np.max(Z), showscale=False), scatter_trace]
    
    frames.append(go.Frame(data=frame_data, name=f'a = {a_val:.2f}'))

    fig.add_trace(scatter_trace)

fig.frames = frames

fig.update_layout(updatemenus=[dict(type='buttons', showactive=False, buttons=[dict(label='Play',
                                method='animate', args=[None, dict(frame=dict(duration=100, redraw=True), fromcurrent=True, mode='immediate')]),
                               dict(label='Pause', method='animate', args=[[None], dict(frame=dict(duration=0, redraw=False), mode='immediate')])])])

fig.update_layout(sliders=[dict(currentvalue=dict(prefix='Speed: ', visible=True),
                                steps=[dict(label=str(duration), method='animate', args=[[None], dict(frame=dict(duration=duration, redraw=True), mode='immediate')]) for duration in [100, 50, 10, 1]])])

fig.update_layout(title='Creative Animated 3D Function Visualization',
                  scene=dict(xaxis_title='x', yaxis_title='a', zaxis_title='Function Value'),
                  scene_camera=dict(eye=dict(x=2.5, y=-1.5, z=1)))  # Adjust the initial camera position

fig.update_layout(scene=dict(aspectmode="cube"))  # Set the scene to be a cube for consistent scaling

fig.show()
