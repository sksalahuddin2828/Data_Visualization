import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import ipywidgets as widgets
from IPython.display import display

def update_wave(A, k, w, phi):
    y = A * np.sin(k * x_values - w * 0 + phi)
    with fig.batch_update():
        fig.data[0].y = y

# Generate x values
x_values = np.linspace(0, 10, 400)

# Initial parameters
initial_A = 0.5
initial_k = 2 * np.pi / 5
initial_w = 2 * np.pi / 2
initial_phi = np.pi / 4

# Create the figure
fig = make_subplots(rows=1, cols=1)
fig.add_trace(go.Scatter(x=x_values, y=initial_A * np.sin(initial_k * x_values - initial_w * 0 + initial_phi),
                         mode='lines', name='Sinusoidal Wave'))

# Create widgets
A_slider = widgets.FloatSlider(value=initial_A, min=0.1, max=1.0, step=0.1, description='Amplitude:')
k_slider = widgets.FloatSlider(value=initial_k, min=0.1, max=5.0, step=0.1, description='Wave Number:')
w_slider = widgets.FloatSlider(value=initial_w, min=0.1, max=5.0, step=0.1, description='Angular Frequency:')
phi_slider = widgets.FloatSlider(value=initial_phi, min=0, max=np.pi, step=0.1, description='Initial Phase:')

# Create interaction
widgets.interact(update_wave, A=A_slider, k=k_slider, w=w_slider, phi=phi_slider)

# Display the figure
fig.show()
