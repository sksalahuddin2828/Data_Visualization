import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation  # Import the animation module
import plotly.graph_objs as go
from ipywidgets import interactive, FloatSlider

# Generate pulse data
x = np.linspace(0, 10, 500)
pulse = np.exp(-0.2 * (x - 3) ** 2) * np.sin(4 * np.pi * x)

# Create pulse animation using Matplotlib
fig, ax = plt.subplots()
line, = ax.plot(x, pulse)

def animate(t):
    line.set_ydata(np.roll(pulse, int(t * 20)))
    return line,

ani = animation.FuncAnimation(fig, animate, frames=np.linspace(0, 10, 200), interval=50, blit=True)
plt.show()

def sinusoidal_wave(x, t, A, k, omega, phi):
    return A * np.sin(k * x - omega * t + phi)

x_values = np.linspace(0, 10, 500)
t_values = np.linspace(0, 2, 200)
A = 1.0
k = 2 * np.pi / 5
omega = 2 * np.pi / 2
phi = 0.0

# Calculate wave data
wave_data = np.array([[sinusoidal_wave(x, t, A, k, omega, phi) for x in x_values] for t in t_values])

def plot_wave(amplitude, wave_number, angular_frequency, initial_phase):
    fig = go.Figure()

    for t in t_values:
        y_values = sinusoidal_wave(x_values, t, amplitude, wave_number, angular_frequency, initial_phase)
        fig.add_trace(go.Scatter(x=x_values, y=y_values, mode='lines', name=f't = {t:.2f}'))

    fig.update_layout(title='Interactive Sinusoidal Wave',
                      xaxis_title='x', yaxis_title='y',
                      xaxis_range=[0, 10], yaxis_range=[-1.5, 1.5])
    fig.show()

interactive_plot = interactive(plot_wave,
                                amplitude=FloatSlider(min=0.1, max=2, step=0.1, value=1),
                                wave_number=FloatSlider(min=0.5, max=5, step=0.5, value=1),
                                angular_frequency=FloatSlider(min=0.5, max=5, step=0.5, value=1),
                                initial_phase=FloatSlider(min=0, max=2 * np.pi, step=0.1, value=0))
interactive_plot
