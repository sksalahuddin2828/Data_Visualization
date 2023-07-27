import plotly.graph_objects as go

def plot_fermat_theorem(limit):
    x_values = []
    y_values = []
    z_values = []
    
    for x in range(1, limit):
        for y in range(x, limit):
            z = np.cbrt(x**3 + y**3)
            if z == int(z):
                continue
            x_values.append(x)
            y_values.append(y)
            z_values.append(z)
    
    fig = go.Figure(data=[go.Scatter3d(x=x_values, y=y_values, z=z_values, mode='markers', 
                                      marker=dict(size=5))])
    fig.update_layout(scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Z'),
                      title='Fermat\'s Last Theorem: x³ + y³ ≠ z³',
                      margin=dict(l=0, r=0, b=0, t=40))
    fig.show()

# Animate the plot to make it more visually appealing
limit = 30
plot_fermat_theorem(limit)
