import numpy as np
import pandas as pd
import sympy as sp
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Given data
galvanometer_sensitivity = 50e-6  # in Amperes
galvanometer_resistance = 25.0  # in Ohms
full_scale_voltage = 3000.0  # in Volts

# Create a function to calculate the unknown resistance
def calculate_unknown_resistance(sensitivity, voltage):
    current_galvanometer = voltage / galvanometer_resistance
    return (voltage / current_galvanometer) - galvanometer_resistance

# Create a grid of sensitivity and voltage values
sensitivity_values = np.linspace(1e-6, 100e-6, 100)
voltage_values = np.linspace(1, 10000, 100)
sensitivity_grid, voltage_grid = np.meshgrid(sensitivity_values, voltage_values)
resistance_grid = np.vectorize(calculate_unknown_resistance)(sensitivity_grid, voltage_grid)

# Create a pandas DataFrame for the grid
df = pd.DataFrame({
    'Sensitivity (A/V)': sensitivity_grid.ravel(),
    'Full-Scale Voltage (V)': voltage_grid.ravel(),
    'Unknown Resistance (Ohms)': resistance_grid.ravel()
})

# Create interactive 3D scatter plot using Plotly
fig = make_subplots(rows=1, cols=1, specs=[[{'type': 'scatter3d'}]])
scatter = go.Scatter3d(
    x=df['Sensitivity (A/V)'],
    y=df['Full-Scale Voltage (V)'],
    z=df['Unknown Resistance (Ohms)'],
    mode='markers',
    marker=dict(size=4),
    text='Unknown Resistance (Ohms)',
    opacity=0.7,
)
fig.add_trace(scatter)
fig.update_layout(
    scene=dict(
        xaxis_title='Sensitivity (A/V)',
        yaxis_title='Full-Scale Voltage (V)',
        zaxis_title='Unknown Resistance (Ohms)',
    ),
    title='Interactive 3D Visualization of Unknown Resistance',
)

# Convert the SymPy equation to a string
expression_str = sp.pretty(expression, use_unicode=True)

# Convert the theory to a string
theory_str = """
When a voltage source of V Volts is connected in series with a galvanometer and an unknown resistance (R),
the current through the circuit can be calculated using Ohm's law:

I = V / (R + RG)

Where:
- I is the current through the circuit.
- V is the applied voltage (in Volts).
- R is the unknown resistance (in Ohms).
- RG is the galvanometer resistance (in Ohms).

By rearranging the equation, we can solve for the unknown resistance R:

R = V / I - RG

In this visualization, we explore the relationship between Sensitivity (A/V), Full-Scale Voltage (V),
and Unknown Resistance (Ohms) using various sensitivity and voltage values.
"""

# Display the additional information
fig.add_annotation(
    text=expression_str,
    x=0.6,
    y=0.85,
    xref="paper",
    yref="paper",
    showarrow=False,
    font=dict(size=10),
)

fig.add_annotation(
    text=theory_str,
    x=0.6,
    y=0.5,
    xref="paper",
    yref="paper",
    showarrow=False,
    font=dict(size=10),
)

# Add animations to visualize changing sensitivity and voltage
frames = []
for i, sensitivity in enumerate(sensitivity_values):
    frame = go.Frame(
        data=[
            go.Scatter3d(
                x=df['Sensitivity (A/V)'][:i],
                y=df['Full-Scale Voltage (V)'][:i],
                z=df['Unknown Resistance (Ohms)'][:i],
                mode='markers',
                marker=dict(size=4),
                text='Unknown Resistance (Ohms)',
                opacity=0.7,
            )
        ],
        name=f'Frame {i}',
    )
    frames.append(frame)

fig.frames = frames

# Define animation settings
animation_settings = dict(
    frame=dict(duration=100, redraw=True),
    fromcurrent=True,
    transition=dict(duration=300, easing="quadratic-in-out"),
)

# Update the layout to include animation controls
fig.update_layout(
    updatemenus=[
        dict(
            type="buttons",
            showactive=False,
            buttons=[
                dict(
                    label="Play",
                    method="animate",
                    args=[
                        None,
                        animation_settings,
                    ],
                ),
                dict(
                    label="Pause",
                    method="animate",
                    args=[
                        [None],
                        animation_settings,
                    ],
                ),
            ],
            x=0.05,
            xanchor="left",
            y=0.05,
            yanchor="bottom",
        ),
    ],
)

# Show the interactive plot in a Jupyter Notebook
fig.show()
