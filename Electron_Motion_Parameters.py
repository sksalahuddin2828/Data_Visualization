import sympy as sp
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Constants
m = 9.11e-31  # Mass of an electron in kg
v = 6.00e7  # Velocity of the electron in m/s
q = 1.60e-19  # Charge of an electron in C
B = 0.500  # Magnetic field strength in T

# Calculate radius of curvature
r = (m * v) / (q * B)

# Create a pandas DataFrame for clear presentation
data = {
    "Quantity": ["Mass (m)", "Velocity (v)", "Charge (q)", "Magnetic Field (B)", "Radius (r)"],
    "Value": [m, v, q, B, r],
    "Unit": ["kg", "m/s", "C", "T", "m"]
}

df = pd.DataFrame(data)

# Create the Dash application
app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(
        id='electron-path',
        figure={
            'data': [
                go.Scatter3d(x=r * np.cos(np.linspace(0, 2 * np.pi, 100)),
                             y=r * np.sin(np.linspace(0, 2 * np.pi, 100)),
                             z=np.linspace(0, 2 * np.pi, 100),
                             mode='lines',
                             name='Electron Path')
            ],
            'layout': go.Layout(
                scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Time'),
                title='Electron Path in Magnetic Field',
                showlegend=True
            )
        }
    ),
    html.H2("Electron Motion Parameters"),
    html.Table([
        html.Tr([html.Th(col) for col in df.columns]),
        html.Tbody([
            html.Tr([
                html.Td(df.iloc[i][col]) for col in df.columns
            ]) for i in range(len(df))
        ])
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)
