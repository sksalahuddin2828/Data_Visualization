import plotly.graph_objects as go

fig = go.Figure(data=[go.Scatter3d(x=[1, 2, 3], y=[4, 5, 6], z=[7, 8, 9], mode='markers')])

# Add an annotation with a shifted position
annotation_x = 1.5
annotation_y = 4.5
annotation_z = 7.5

fig.add_trace(go.Scatter3d(x=[annotation_x], y=[annotation_y], z=[annotation_z], 
                           mode='markers+text', text='Annotation',
                           marker=dict(size=5, color='red'), textposition='top center'))

fig.update_layout(scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Z'),
                  title='3D Scatter Plot with Annotation')

fig.show()
