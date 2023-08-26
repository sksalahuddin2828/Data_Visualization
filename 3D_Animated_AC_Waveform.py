import numpy as np
import plotly.graph_objects as go

# Create a time array
t = np.linspace(0, 2 * np.pi, 100)

# Create sine wave data
V = np.sin(t)
I = np.cos(t)

# Create an animated line plot
fig = go.Figure()

fig.add_trace(go.Scatter(x=t, y=V, mode='lines', name='Voltage'))
fig.add_trace(go.Scatter(x=t, y=I, mode='lines', name='Current'))

fig.update_layout(title='Animated AC Waveform', xaxis_title='Time', yaxis_title='Amplitude')

frames = [go.Frame(data=[go.Scatter(x=t[:i+1], y=V[:i+1]),
                         go.Scatter(x=t[:i+1], y=I[:i+1])],
                   name=str(i))
          for i in range(1, len(t))]

fig.frames = frames

fig.show()
