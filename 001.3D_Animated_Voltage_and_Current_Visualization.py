import numpy as np
import pandas as pd
import plotly.graph_objects as go
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

# Create a subplot for each frequency
fig = make_subplots(rows=len(freqs), cols=1, shared_xaxes=True, vertical_spacing=0.1)

# Add traces for voltage and current for each frequency
for i, f in enumerate(freqs):
    fig.add_trace(go.Scatter(x=df['Time'], y=df[f'Voltage_{f}Hz'], mode='lines', name=f'Voltage @ {f} Hz'), row=i+1, col=1)
    fig.add_trace(go.Scatter(x=df['Time'], y=df[f'Current_{f}Hz'], mode='lines', name=f'Current @ {f} Hz'), row=i+1, col=1)

# Define colors for phase difference
color_map = {50: 'blue', 100: 'green', 200: 'orange', 300: 'red'}

# Create frames for animation
frames = []
for i, f in enumerate(freqs):
    frame = go.Frame(data=[go.Scatter(x=df['Time'], y=df[f'Voltage_{f}Hz'], mode='lines', name=f'Voltage @ {f} Hz'),
                           go.Scatter(x=df['Time'], y=df[f'Current_{f}Hz'], mode='lines', name=f'Current @ {f} Hz',
                                      line=dict(color=color_map[f]))],
                     name=str(f))
    frames.append(frame)

# Update layout for animation
fig.frames = frames
animation_settings = dict(frame=dict(duration=500, redraw=True), fromcurrent=True)
fig.update_layout(updatemenus=[dict(type='buttons', showactive=False, buttons=[dict(label='Play',
                                    method='animate', args=[None, animation_settings])])])

# Set axis labels and title
fig.update_xaxes(title_text='Time')
fig.update_yaxes(title_text='Value')
fig.update_layout(title='Animated Voltage and Current Visualization')

# Show the animated plot
fig.show()
