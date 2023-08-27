import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import sympy as sp

# Create data
rms_values = np.linspace(0, 20, 100)
peak_values = rms_values * np.sqrt(2)
data = pd.DataFrame({'RMS Current (A)': rms_values, 'Peak Current (A)': peak_values})

# Create sinusoidal waveform data for animation
time_values = np.linspace(0, 2*np.pi, 100)
waveform = np.sin(time_values)
waveform_data = pd.DataFrame({'Time': time_values, 'Waveform': waveform})

# Create interactive animation subplot
fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.1,
                    subplot_titles=["RMS vs. Peak Current", "Sinusoidal Waveform"])

# Add scatter plot for RMS vs. Peak Current
scatter_trace = go.Scatter(x=data['RMS Current (A)'], y=data['Peak Current (A)'],
                           mode='markers', marker=dict(size=8),
                           hovertemplate='RMS Current: %{x:.2f} A<br>Peak Current: %{y:.2f} A')
fig.add_trace(scatter_trace, row=1, col=1)

# Add animation trace for sinusoidal waveform
animation_trace = go.Scatter(x=[waveform_data['Time'][0]], y=[waveform_data['Waveform'][0]],
                             mode='lines', line=dict(color='blue'), showlegend=False)
fig.add_trace(animation_trace, row=2, col=1)

# Configure animation settings
frames = [go.Frame(data=[go.Scatter(x=waveform_data['Time'][:i+1], y=waveform_data['Waveform'][:i+1])],
                   name=str(i)) for i in range(1, len(waveform_data))]

for frame in frames:
    fig.add_frame(frame)

# Update layout
fig.update_layout(updatemenus=[dict(type='buttons', showactive=False, buttons=[dict(label='Play',
                         method='animate', args=[None, dict(frame=dict(duration=50, redraw=True),
                         fromcurrent=True, transition=dict(duration=0)]))])])

# Add equations and annotations
eq_text = "Peak Current = RMS Current × √2"
fig.add_annotation(text=eq_text, x=10, y=15, showarrow=False)

theory_text = "The Root Mean Square (RMS) current is the effective current of an alternating current waveform. " \
              "The Peak Current is √2 times the RMS current for a sinusoidal waveform."
fig.add_annotation(text=theory_text, x=0.5, y=1.1, xref="paper", yref="paper", showarrow=False)

# Update axis labels and titles
fig.update_xaxes(title_text="RMS Current (A)", row=1, col=1)
fig.update_yaxes(title_text="Peak Current (A)", row=1, col=1)
fig.update_xaxes(title_text="Time", row=2, col=1)
fig.update_yaxes(title_text="Amplitude", row=2, col=1)

fig.update_layout(title_text="Understanding RMS and Peak Current Relationship with Sinusoidal Waveform",
                  height=800)

# Show the interactive animation
fig.show()
