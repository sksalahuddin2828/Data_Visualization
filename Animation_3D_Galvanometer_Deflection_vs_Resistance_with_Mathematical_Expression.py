import numpy as np
import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import sympy as sp

# Constants
V_full_scale = 0.100  # Full-scale reading in volts
I_g_sensitivity = 50e-6  # Galvanometer sensitivity in amperes
G_internal_resistance = 25.0  # Internal resistance of the galvanometer in ohms

# Create a symbolic variable for resistance
R_symbolic = sp.symbols('R')

# Calculate the voltmeter reading using a symbolic expression
V_meter_expression = V_full_scale / (1 + R_symbolic / G_internal_resistance)

# Calculate the galvanometer deflection using a symbolic expression
Galvanometer_deflection_expression = I_g_sensitivity * (V_meter_expression - V_full_scale) + G_internal_resistance * (V_meter_expression / V_full_scale - 1)

# Create a function to calculate deflection for a given resistance
calculate_deflection = sp.lambdify(R_symbolic, Galvanometer_deflection_expression, 'numpy')

# Create a range of resistance values
R_values = np.linspace(0, 200, 100)  # You can adjust the range as needed

# Calculate deflection for each resistance value
deflection_values = calculate_deflection(R_values)

# Create a DataFrame for visualization
df = pd.DataFrame({'Resistance (Ω)': R_values, 'Galvanometer Deflection (A)': deflection_values})

# Find the minimum resistance needed for accurate measurement
min_R = df.loc[df['Galvanometer Deflection (A)'].abs().idxmin(), 'Resistance (Ω)']

# Create an animated Plotly figure
fig = make_subplots(rows=2, cols=2, specs=[[{}, {}], [{'colspan': 2}, None]],
                    subplot_titles=('Resistance vs. Galvanometer Deflection',
                                    'Minimum Resistance for Accurate Measurement'))

# Scatter plot for Resistance vs. Galvanometer Deflection
trace1 = go.Scatter(x=df['Resistance (Ω)'], y=df['Galvanometer Deflection (A)'], mode='lines', name='Galvanometer Deflection (A)')
fig.add_trace(trace1, row=1, col=1)

# Horizontal line at 0 for Galvanometer Deflection
trace2 = go.Scatter(x=df['Resistance (Ω)'], y=np.zeros_like(df['Resistance (Ω)']), mode='lines', name='Zero Deflection',
                    line=dict(color='red', dash='dash'))
fig.add_trace(trace2, row=1, col=1)

# Display minimum resistance needed
fig.add_annotation(text=f"Minimum Resistance: {min_R:.2f} Ω", showarrow=False, xref='paper', yref='paper', x=0.5, y=0.15,
                   font=dict(size=14))

# Create an animated slider to show the mathematical expression
frames = [go.Frame(data=[go.Scatter(x=df['Resistance (Ω)'], y=[calculate_deflection(R_values[i])]*len(R_values), mode='lines')],
                   name=f"Frame {i+1}") for i in range(len(R_values))]

fig.frames = frames  # Set frames directly

# Update axis labels and layout
fig.update_xaxes(title_text='Resistance (Ω)', row=1, col=1)
fig.update_yaxes(title_text='Deflection (A)', row=1, col=1)
fig.update_layout(title='Galvanometer Deflection vs. Resistance with Mathematical Expression',
                  height=600, width=800, showlegend=True)

# Create a list of steps for the animation
steps = []
for i in range(len(R_values)):
    step = {
        'args': [
            [f"Frame {i+1}"],
            {
                'frame': {'duration': 500, 'redraw': True},
                'mode': 'immediate',
                'transition': {'duration': 0},
            },
        ],
        'label': f"Frame {i+1}",
        'method': 'animate',
    }
    steps.append(step)

# Create and add the animation slider
sliders = [
    {
        'active': 0,
        'steps': steps,
        'yanchor': 'top',
        'xanchor': 'left',
        'currentvalue': {
            'font': {'size': 16},
            'prefix': 'Frame:',
            'visible': True,
            'xanchor': 'right',
        },
        'transition': {'duration': 0, 'easing': 'linear'},
        'len': 0.9,
        'x': 0.1,
        'y': 0,
    }
]

fig.update_layout(sliders=sliders)

# Show the interactive Plotly figure
fig.show()
