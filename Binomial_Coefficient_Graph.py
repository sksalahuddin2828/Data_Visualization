import numpy as np
import pandas as pd
import plotly.graph_objects as go

def binomial_coefficient(n, k):
    if k == 0:
        return 1
    return (n * binomial_coefficient(n - 1, k - 1)) // k

n_vals = [2, 3, 4, 5]
terms = 10

data = []

for n in n_vals:
    expansion_coeffs = [binomial_coefficient(n, k) * (-1)**k for k in range(terms)]
    data.append([n] + expansion_coeffs)

columns = ['n'] + [f'Coefficient {k}' for k in range(terms)]
df = pd.DataFrame(data, columns=columns)

table_fig = go.Figure(data=[go.Table(header=dict(values=df.columns),
                 cells=dict(values=[df['n']] + [df[f'Coefficient {k}'] for k in range(terms)]))])
table_fig.show()
