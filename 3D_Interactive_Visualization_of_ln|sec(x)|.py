# pip install dash

import numpy as np
import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import sympy as sp

# Calculate integral
x = sp.symbols('x')
integral_expr = sp.integrate(sp.tan(x), x)

# Generate data
x_vals = np.linspace(-2*np.pi, 2*np.pi, 400)
y_vals = np.log(np.abs(1/np.cos(x_vals)))

# Create a DataFrame for pandas
data = {'x': x_vals, 'ln|sec(x)|': y_vals}
df = pd.DataFrame(data)

# Create the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1("Interactive Dashboard: ln|sec(x)|"),
    
    dcc.Graph(id='plot', config={'displayModeBar': False}),
    
    dcc.Slider(
        id='x-slider',
        min=-2*np.pi,
        max=2*np.pi,
        step=0.01,
        value=0,
        marks={-2*np.pi: '-2π', -np.pi: '-π', 0: '0', np.pi: 'π', 2*np.pi: '2π'},
    ),
    
    html.Div(id='output-text')
])

# Define callback functions
@app.callback(
    Output('plot', 'figure'),
    Output('output-text', 'children'),
    Input('x-slider', 'value')
)
def update_plot(selected_x):
    selected_y = np.log(np.abs(1/np.cos(selected_x)))
    
    fig = px.line(df, x='x', y='ln|sec(x)|', title="Interactive Visualization of ln|sec(x)|")
    fig.add_trace(px.scatter(x=[selected_x], y=[selected_y], mode='markers', name='Selected Point'))
    
    output_text = f"At x = {selected_x:.2f}, ln|sec(x)| = {selected_y:.2f}"
    
    return fig, output_text

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
