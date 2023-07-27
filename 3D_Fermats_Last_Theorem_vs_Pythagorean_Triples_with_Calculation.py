import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def fermat_last_theorem(limit):
    x_values = []
    y_values = []
    z_values = []
    valid_solution = False
    
    for x in range(1, limit):
        for y in range(x, limit):
            z = np.cbrt(x**3 + y**3)
            if z == int(z):
                valid_solution = True
                x_values.append(x)
                y_values.append(y)
                z_values.append(z)
    
    return x_values, y_values, z_values, valid_solution

def calculate_valid_solutions_percentage(limit):
    x, y, z, valid_solution = fermat_last_theorem(limit)
    total_combinations = (limit * (limit - 1)) // 2
    valid_combinations = len(x) if valid_solution else 0
    percentage = (valid_combinations / total_combinations) * 100
    return percentage

def plot_fermat_theorem(limit):
    x, y, z, valid_solution = fermat_last_theorem(limit)
    percentage = calculate_valid_solutions_percentage(limit)

    fig = make_subplots(rows=1, cols=2, specs=[[{'type': 'scatter3d'}]*2],
                        subplot_titles=['Fermat\'s Last Theorem: x³ + y³ ≠ z³',
                                        'Pythagorean Triples: x² + y² = z²'],
                        horizontal_spacing=0.1)
    
    if valid_solution:
        fig.add_trace(go.Scatter3d(x=x, y=y, z=z, mode='markers',
                                   marker=dict(size=5, color='red'),
                                   name='Invalid Solutions'), row=1, col=1)
    else:
        fig.add_trace(go.Scatter3d(x=[], y=[], z=[], mode='markers',
                                   marker=dict(size=5, color='red'),
                                   name='No Integer Solutions'), row=1, col=1)
    
    # Generate Pythagorean Triples for comparison
    pythagorean_triples = []
    for x in range(1, limit):
        for y in range(x, limit):
            z = np.sqrt(x**2 + y**2)
            if z == int(z):
                pythagorean_triples.append((x, y, int(z)))
    
    x_pt = [triple[0] for triple in pythagorean_triples]
    y_pt = [triple[1] for triple in pythagorean_triples]
    z_pt = [triple[2] for triple in pythagorean_triples]
    
    fig.add_trace(go.Scatter3d(x=x_pt, y=y_pt, z=z_pt, mode='markers',
                               marker=dict(size=5, color='blue'),
                               name='Pythagorean Triples'), row=1, col=2)
    
    fig.update_layout(scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Z'),
                      title='Fermat\'s Last Theorem vs. Pythagorean Triples',
                      margin=dict(l=0, r=0, b=0, t=50))
    
    if valid_solution:
        fig.update_layout(annotations=[
            dict(
                x=np.mean(x),
                y=np.mean(y),
                z=np.mean(z),
                text='No Integer Solutions for x³ + y³ = z³',
                showarrow=True,
                arrowhead=1,
                ax=0,
                ay=-40,
                ayref='y',
                bgcolor='white',
                opacity=0.8
            )
        ])
    
    fig.update_layout(width=900, height=500)

    # Add mathematical equations and annotations
    fig.add_annotation(
        go.layout.Annotation(
            x=0.06, y=0.1,
            xref='paper', yref='paper',
            text="Fermat's Last Theorem:",
            font=dict(size=14, color='black'),
            showarrow=False
        )
    )

    fig.add_annotation(
        go.layout.Annotation(
            x=0.06, y=0.05,
            xref='paper', yref='paper',
            text=r"$x^3 + y^3 \neq z^3$",
            font=dict(size=18, color='black'),
            showarrow=False
        )
    )

    fig.add_annotation(
        go.layout.Annotation(
            x=0.52, y=0.1,
            xref='paper', yref='paper',
            text="Pythagorean Triples:",
            font=dict(size=14, color='black'),
            showarrow=False
        )
    )

    fig.add_annotation(
        go.layout.Annotation(
            x=0.52, y=0.05,
            xref='paper', yref='paper',
            text=r"$x^2 + y^2 = z^2$",
            font=dict(size=18, color='black'),
            showarrow=False
        )
    )

    # Add information about valid solutions and percentage
    if valid_solution:
        fig.add_annotation(
            go.layout.Annotation(
                x=0.75, y=0.9,
                xref='paper', yref='paper',
                text=f"Valid Solutions: {len(x)}",
                font=dict(size=14, color='black'),
                showarrow=False
            )
        )
    else:
        fig.add_annotation(
            go.layout.Annotation(
                x=0.75, y=0.9,
                xref='paper', yref='paper',
                text="No Valid Solutions",
                font=dict(size=14, color='black'),
                showarrow=False
            )
        )

    fig.add_annotation(
        go.layout.Annotation(
            x=0.75, y=0.85,
            xref='paper', yref='paper',
            text=f"Total Combinations: {(limit * (limit - 1)) // 2}",
            font=dict(size=14, color='black'),
            showarrow=False
        )
    )

    fig.add_annotation(
        go.layout.Annotation(
            x=0.75, y=0.8,
            xref='paper', yref='paper',
            text=f"Valid Solutions Percentage: {percentage:.2f}%",
            font=dict(size=14, color='black'),
            showarrow=False
        )
    )

    fig.show()

# Set the limit for exploration
limit = 30
plot_fermat_theorem(limit)
