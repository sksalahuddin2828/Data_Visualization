import numpy as np
import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots

# Constants
V_full_scale = 0.100  # Full-scale reading in volts
I_g_sensitivity = 50e-6  # Galvanometer sensitivity in amperes
G_internal_resistance = 25.0  # Internal resistance of the galvanometer in ohms

# Create a range of resistance values
R = np.linspace(0, 200, 100)  # You can adjust the range as needed

# Calculate the voltmeter reading for each resistance value
V_meter = V_full_scale / (1 + R / G_internal_resistance)

# Create a DataFrame for visualization
df = pd.DataFrame({'Resistance (Ω)': R, 'Voltmeter Reading (V)': V_meter})

# Calculate galvanometer deflection for each resistance value
df['Galvanometer Deflection (A)'] = I_g_sensitivity * (df['Voltmeter Reading (V)'] - V_full_scale) + G_internal_resistance * (df['Voltmeter Reading (V)'] / V_full_scale - 1)

# Find the minimum resistance needed for accurate measurement
min_R = df.loc[df['Galvanometer Deflection (A)'].abs().idxmin(), 'Resistance (Ω)']

# Create a Plotly figure
fig = make_subplots(rows=2, cols=2, specs=[[{}, {}], [{'colspan': 2}, None]],
                    subplot_titles=('Resistance vs. Voltmeter Reading',
                                    'Resistance vs. Galvanometer Deflection',
                                    'Minimum Resistance for Accurate Measurement'))

# Scatter plot for Resistance vs. Voltmeter Reading
trace1 = go.Scatter(x=df['Resistance (Ω)'], y=df['Voltmeter Reading (V)'], mode='lines', name='Voltmeter Reading (V)')
fig.add_trace(trace1, row=1, col=1)

# Scatter plot for Resistance vs. Galvanometer Deflection
trace2 = go.Scatter(x=df['Resistance (Ω)'], y=df['Galvanometer Deflection (A)'], mode='lines', name='Galvanometer Deflection (A)')
fig.add_trace(trace2, row=1, col=2)

# Horizontal line at 0 for Galvanometer Deflection
trace3 = go.Scatter(x=df['Resistance (Ω)'], y=np.zeros_like(df['Resistance (Ω)']), mode='lines', name='Zero Deflection',
                    line=dict(color='red', dash='dash'))
fig.add_trace(trace3, row=1, col=2)

# Display minimum resistance needed
fig.add_annotation(text=f"Minimum Resistance: {min_R:.2f} Ω", showarrow=False, xref='paper', yref='paper', x=0.5, y=0.15,
                   font=dict(size=14))

# Update axis labels and layout
fig.update_xaxes(title_text='Resistance (Ω)', row=1, col=1)
fig.update_xaxes(title_text='Resistance (Ω)', row=1, col=2)
fig.update_yaxes(title_text='Voltage (V)', row=1, col=1)
fig.update_yaxes(title_text='Deflection (A)', row=1, col=2)
fig.update_layout(title='Voltage Measurement with Galvanometer',
                  height=600, width=800, showlegend=True)

# Show the interactive Plotly figure
fig.show()
