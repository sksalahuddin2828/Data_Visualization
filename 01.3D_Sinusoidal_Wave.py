import plotly.graph_objects as go

def sinusoidal_wave(x, t, A, k, w, phi):
    return A * np.sin(k*x - w*t + phi)

x_values = np.linspace(0, 10, 100)
t_values = np.linspace(0, 10, 100)
A = 1.0  # Amplitude
k = 2*np.pi/5  # Wave number
w = 2*np.pi/2  # Angular frequency
phi = 0  # Initial phase

fig = go.Figure()

for t in t_values:
    y_values = sinusoidal_wave(x_values, t, A, k, w, phi)
    fig.add_trace(go.Scatter(x=x_values, y=y_values, mode='lines', name=f't={t:.1f}s'))

fig.update_layout(
    title='Sinusoidal Wave',
    xaxis_title='x (m)',
    yaxis_title='Amplitude',
    xaxis=dict(range=[0, 10]),
    yaxis=dict(range=[-1.5, 1.5]),
    updatemenus=[dict(
        type='buttons',
        showactive=False,
        buttons=[dict(label='Play',
                      method='animate',
                      args=[None, {'frame': {'duration': 100, 'redraw': True}, 'fromcurrent': True}]),
                 dict(label='Pause',
                      method='animate',
                      args=[[None], {'frame': {'duration': 0, 'redraw': False}, 'mode': 'immediate'}])]
    )]
)

frames = [go.Frame(data=[go.Scatter(x=x_values, y=sinusoidal_wave(x_values, t, A, k, w, phi))],
                   name=f'Frame {i}',
                   traces=[0]) for i, t in enumerate(t_values)]

fig.update(frames=frames)

fig.show()
