import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display

# Function to update and display trigonometric calculations and plot
def update_trig(angle_degrees):
    angle_radians = np.deg2rad(angle_degrees)
    sin_value = np.sin(angle_radians)
    cos_value = np.cos(angle_radians)
    tan_value = np.tan(angle_radians)

    trig_results = widgets.HTML(
        value=f"<strong>Results:</strong><br>Sine({angle_degrees}°) = {sin_value:.4f}<br>Cosine({angle_degrees}°) = {cos_value:.4f}<br>Tangent({angle_degrees}°) = {tan_value:.4f}"
    )

    theta_degrees = np.linspace(0, 360, 360)
    sin_values = np.sin(np.deg2rad(theta_degrees))
    cos_values = np.cos(np.deg2rad(theta_degrees))

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(theta_degrees, sin_values, label='sin(Theta)')
    ax.plot(theta_degrees, cos_values, label='cos(Theta)')
    ax.set_xlabel('Angle (Degrees)')
    ax.set_ylabel('Value')
    ax.set_title(f'Sine and Cosine Functions for θ = {angle_degrees}°')
    ax.legend()
    plt.show()

angle_input = widgets.FloatSlider(
    value=0, min=0, max=360, step=1, description='Angle (Degrees)'
)
widgets.interactive(update_trig, angle_degrees=angle_input)


#------------------------------------------------------------------------------------------------------


import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc

# Create a Dash web application
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Layout of the web app
app.layout = html.Div([
    html.H1("Trigonometric Function Explorer"),
    html.Label("Enter an angle in degrees:"),
    dcc.Input(id="angle-input", type="number", value=0, step=1),
    html.Div(id="trig-results"),
    dcc.Graph(id="trig-plot")
])

# Callback to update trigonometric calculations and plot
@app.callback(
    [Output("trig-results", "children"), Output("trig-plot", "figure")],
    [Input("angle-input", "value")]
)
def update_trig(angle_degrees):
    angle_radians = np.deg2rad(angle_degrees)
    sin_value = np.sin(angle_radians)
    cos_value = np.cos(angle_radians)
    tan_value = np.tan(angle_radians)

    trig_results = html.Div([
        html.P(f"Sine({angle_degrees}°) = {sin_value:.4f}"),
        html.P(f"Cosine({angle_degrees}°) = {cos_value:.4f}"),
        html.P(f"Tangent({angle_degrees}°) = {tan_value:.4f}")
    ])

    theta_degrees = np.linspace(0, 360, 360)
    sin_values = np.sin(np.deg2rad(theta_degrees))
    cos_values = np.cos(np.deg2rad(theta_degrees))

    df = pd.DataFrame({'Theta': theta_degrees, 'sin(Theta)': sin_values, 'cos(Theta)': cos_values})

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['Theta'], y=df['sin(Theta)'], mode='lines', name='sin(Theta)'))
    fig.add_trace(go.Scatter(x=df['Theta'], y=df['cos(Theta)'], mode='lines', name='cos(Theta)'))
    fig.update_xaxes(title='Angle (Degrees)')
    fig.update_yaxes(title='Value')
    fig.update_layout(title=f'Sine and Cosine Functions for θ = {angle_degrees}°')

    return trig_results, fig

if __name__ == '__main__':
    app.run_server(debug=True)
