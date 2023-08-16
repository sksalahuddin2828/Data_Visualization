import numpy as np
import plotly.graph_objects as go

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

fig = go.Figure()

for n in n_vals:
    y_vals = [binomial_expansion(x, n, terms) for x in x_vals]
    fig.add_trace(go.Scatter(x=x_vals, y=y_vals, mode='lines', name=f'n = {n}'))

fig.update_layout(title='Binomial Expansion of (1+x)^n using Binomial Coefficients',
                  xaxis_title='x', yaxis_title='(1+x)^n')
fig.show()
