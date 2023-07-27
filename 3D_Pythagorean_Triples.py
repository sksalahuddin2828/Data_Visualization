import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def generate_pythagorean_triples(limit):
    triples = []
    for x in range(1, limit):
        for y in range(x, limit):
            z = np.sqrt(x**2 + y**2)
            if z == int(z):
                triples.append((x, y, int(z)))
    return triples

def generate_fermat_solutions(limit):
    solutions = []
    for x in range(1, limit):
        for y in range(x, limit):
            z = np.cbrt(x**3 + y**3)
            if z == int(z):
                continue
            solutions.append((x, y, int(z)))
    return solutions

def create_animation(limit, animation_speed=500):
    pythagorean_triples = generate_pythagorean_triples(limit)
    fermat_solutions = generate_fermat_solutions(limit)

    fig = make_subplots(rows=1, cols=2, specs=[[{'type': 'scatter3d'}]*2],
                        subplot_titles=['Exploring Pythagorean Triples: x² + y² = z²',
                                        'Realizing Fermat\'s Last Theorem: x³ + y³ ≠ z³'],
                        horizontal_spacing=0.1)
    
    for x, y, z in pythagorean_triples:
        fig.add_trace(go.Scatter3d(x=[x], y=[y], z=[z], mode='markers',
                                   marker=dict(size=5, color='blue'),
                                   name='Pythagorean Triples'), row=1, col=1)

    fig.add_trace(go.Scatter3d(x=[], y=[], z=[], mode='markers',
                               marker=dict(size=5, color='red'),
                               name='Invalid Solutions'), row=1, col=2)

    fig.update_layout(scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Z'),
                      title='Journey from Pythagorean Triples to Fermat\'s Last Theorem',
                      margin=dict(l=0, r=0, b=0, t=50))

    buttons = []
    step_duration = animation_speed

    for step in range(len(pythagorean_triples) + 1):
        visible_pythagorean = [False] * len(pythagorean_triples)
        visible_fermat = [False] * len(fermat_solutions)

        if step < len(pythagorean_triples):
            visible_pythagorean[step] = True
        else:
            visible_fermat[0] = True

        # Update the visibility of markers in each subplot
        buttons.append(dict(args=[{'visible': visible_pythagorean},
                                  {'visible': visible_fermat}],
                            label=f'Step {step+1}',
                            method='update'))

    sliders = [dict(active=len(pythagorean_triples), pad={'t': 50},
                    steps=buttons, currentvalue={'visible': False},
                    transition={'duration': step_duration, 'easing': 'cubic-in-out'})]

    fig.update_layout(updatemenus=[dict(type='buttons', showactive=False,
                                        buttons=buttons, x=0.1, y=1.1)],
                      sliders=sliders)

    fig.update_layout(width=900, height=500)
    fig.show()

# Set the limit for exploration
limit = 30
create_animation(limit, animation_speed=500)
