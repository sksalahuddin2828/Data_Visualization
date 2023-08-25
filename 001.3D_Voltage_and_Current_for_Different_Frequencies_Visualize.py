import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from plotly.subplots import make_subplots
import plotly.express as px

# Parameters
V0 = 10  # Peak voltage
R = 5    # Resistance

# Time array
t = np.linspace(0, 0.1, 1000)  # 0 to 0.1 seconds, 1000 data points

# Create a DataFrame to store data for different frequencies
freqs = [50, 100, 200, 300]  # Frequencies to visualize
data_dict = {'Time': t}
for f in freqs:
    V = V0 * np.sin(2 * np.pi * f * t)
    I = V / R
    data_dict[f'Voltage_{f}Hz'] = V
    data_dict[f'Current_{f}Hz'] = I

df = pd.DataFrame(data_dict)

# Create subplots
fig = make_subplots(rows=len(freqs), cols=1, shared_xaxes=True, vertical_spacing=0.1)

for i, f in enumerate(freqs):
    fig.add_trace(go.Scatter(x=df['Time'], y=df[f'Voltage_{f}Hz'], mode='lines', name=f'Voltage @ {f} Hz'), row=i+1, col=1)
    fig.add_trace(go.Scatter(x=df['Time'], y=df[f'Current_{f}Hz'], mode='lines', name=f'Current @ {f} Hz'), row=i+1, col=1)

# Update layout
fig.update_layout(title='Voltage and Current for Different Frequencies', showlegend=False)

# Add a slider to control frequency
slider = go.layout.Updatemenu(type='buttons', showactive=False, buttons=[
    {'label': '50 Hz', 'method': 'update', 'args': [{'visible': [True, True, False, False]}, {'title': 'Voltage and Current at 50 Hz'}]},
    {'label': '100 Hz', 'method': 'update', 'args': [{'visible': [False, False, True, True]}, {'title': 'Voltage and Current at 100 Hz'}]},
    {'label': '200 Hz', 'method': 'update', 'args': [{'visible': [False, False, False, False, True, True, False, False]}, {'title': 'Voltage and Current at 200 Hz'}]},
    {'label': '300 Hz', 'method': 'update', 'args': [{'visible': [False, False, False, False, False, False, True, True]}, {'title': 'Voltage and Current at 300 Hz'}]}
])

fig.update_layout(updatemenus=[slider], height=800)

# Show the plot
fig.show()
