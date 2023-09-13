import numpy as np
import sympy as sp
import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Initialize the Dash app
app = dash.Dash(__name__)

# Define known values
v_electron = 6.00e7  # Speed of the electron in m/s
B_earth = 5.00e-5  # Strength of Earth's magnetic field in T
d = 0.01  # Separation between plates in meters

# Calculate the required electric field strength
e = 1.602e-19  # Elementary charge in coulombs
m_electron = 9.109e-31  # Mass of an electron in kg
E_required = v_electron * B_earth

# Calculate the voltage applied
V = E_required * d

# Create a DataFrame for presentation
data = {'Parameter': ['Speed of Electron', 'Strength of Earth\'s Magnetic Field', 'Separation Between Plates', 'Charge of Electron', 'Mass of Electron', 'Required Electric Field', 'Voltage Applied'],
        'Value': [v_electron, B_earth, d, e, m_electron, E_required, V],
        'Unit': ['m/s', 'T', 'm', 'C', 'kg', 'N/C', 'V']}
df = pd.DataFrame(data)

# Create a 3D plot to visualize the electron's motion
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

t = np.linspace(0, 1e-6, 1000)
x = v_electron * t
y = np.zeros_like(t)
z = np.zeros_like(t)

ax.plot(x, y, z, label='Electron Path', lw=2)

ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_zlabel('Z (m)')
ax.legend()

plt.title("Electron Motion in CRT")

# Define the layout of the Dash app
app.layout = html.Div([
    html.H1("CRT Electron Motion Analysis", style={'textAlign': 'center'}),
    
    # Display the 3D plot
    dcc.Graph(figure={'data': [go.Figure(data=[go.Scatter3d(x=x, y=y, z=z, mode='lines', line=dict(width=2), name='Electron Path')]),
                        'layout': go.Layout(scene=dict(aspectmode="cube"),
                                            scene_camera=dict(eye=dict(x=1.5, y=1.5, z=1.5)),
                                            scene=dict(xaxis_title="X (m)", yaxis_title="Y (m)", zaxis_title="Z (m)"))}),
    
    # Display the table
    html.H2("Parameter Values", style={'textAlign': 'center'}),
    dcc.Graph(id='parameter-table', config={'displayModeBar': False}),
    
    # Display results
    html.Div([
        html.H3("Results", style={'textAlign': 'center'}),
        html.P(f"(a) Required electric field strength: {E_required:.2e} N/C"),
        html.P(f"(b) Voltage applied: {V:.2f} V")
    ])
])

# Define a callback to update the table
@app.callback(
    Output('parameter-table', 'figure'),
    Input('parameter-table', 'id')
)
def update_table(id):
    return go.Figure(data=[go.Table(
        header=dict(values=["Parameter", "Value", "Unit"]),
        cells=dict(values=[df['Parameter'], df['Value'], df['Unit']]))])

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)
