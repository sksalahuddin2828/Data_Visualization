import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def binomial_coefficient(n, k):
    if k == 0:
        return 1
    return (n * binomial_coefficient(n - 1, k - 1)) // k

def binomial_expansion(x, n, terms=5):
    expansion = []
    for k in range(terms):
        term = binomial_coefficient(n, k) * (x ** k)
        expansion.append(term)
    return sum(expansion)

x_vals = np.linspace(-1, 1, 100)
n_vals = [2, 3, 4, 5]
terms = 10

# Create an animation of the binomial expansion for different n values
animation_frames = []
for n in n_vals:
    y_vals = [binomial_expansion(x, n, terms) for x in x_vals]
    frame = go.Frame(data=[go.Scatter(x=x_vals, y=y_vals, mode='lines', name=f'n = {n}')])
    animation_frames.append(frame)

fig = make_subplots(rows=2, cols=2, subplot_titles=[f'n = {n}' for n in n_vals])
fig.update_layout(title_text='Interactive Binomial Expansion Animation',
                  xaxis_title='x', yaxis_title='(1+x)^n')

for n in n_vals:
    y_vals = [binomial_expansion(x, n, terms) for x in x_vals]
    fig.add_trace(go.Scatter(x=x_vals, y=y_vals, mode='lines', name=f'n = {n}'))

fig.frames = animation_frames

# Add slider for animation control
sliders = [dict(steps=[dict(args=[{'visible': [False] * len(fig.data)}, {'visible': [True] * (n + 1)}],
                            label=f'n = {n}', method='update') for n in range(len(n_vals))],
                active=0, transition={'duration': 300})]
fig.update_layout(updatemenus=[dict(type='buttons', showactive=False, buttons=[dict(label='Play',
                                  method='animate', args=[None, {'frame': {'duration': 500, 'redraw': True},
                                                              'fromcurrent': True, 'transition': {'duration': 300}}])])],
                  sliders=sliders)

fig.show()

data = []

for n in n_vals:
    expansion_coeffs = [binomial_coefficient(n, k) * (-1)**k for k in range(terms)]
    data.append(expansion_coeffs)

coeff_df = pd.DataFrame(data, columns=[f'Coefficient {k}' for k in range(terms)], index=n_vals)

heatmap_fig = go.Figure(data=go.Heatmap(z=coeff_df.values, x=coeff_df.columns, y=coeff_df.index, colorscale='Viridis'))
heatmap_fig.update_layout(title='Binomial Coefficients Heatmap',
                         xaxis_title='k (Term index)', yaxis_title='n')
heatmap_fig.show()
