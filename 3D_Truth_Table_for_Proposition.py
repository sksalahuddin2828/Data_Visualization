import plotly.graph_objects as go
import pandas as pd
from sympy.logic.boolalg import truth_table
from sympy.abc import x, y, z

# Define the propositions
propositions = [
    x & ~x,
    (x & (x >> y)) >> ~y,
    ((x >> y) & (y >> z)) & (x & ~z),
    ~(x >> y) | (~x | (x & y)),
    (x == z) >> (~y >> (x & z))
]

# Generate truth tables for propositions
def generate_truth_table(expression):
    tt = truth_table(expression, [x, y, z])
    return tt

# Create interactive tables using Plotly
for i, prop in enumerate(propositions):
    rows = list(generate_truth_table(prop))
    header = ['x', 'y', 'z', 'Result']
    data = [[str(val) for val in row] for row in rows]
    
    fig = go.Figure(data=[go.Table(
        header=dict(values=header),
        cells=dict(values=data))
    ])

    fig.update_layout(title=f"Truth Table for Proposition {i+1}")
    fig.show()
