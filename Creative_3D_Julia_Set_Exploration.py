import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def julia_set(width, height, c_real, c_imag, max_iter=100):
    x_min, x_max = -2.0, 2.0
    y_min, y_max = -2.0, 2.0
    x, y = np.linspace(x_min, x_max, width), np.linspace(y_min, y_max, height)
    X, Y = np.meshgrid(x, y)
    z = X + 1j * Y
    julia = np.zeros_like(z, dtype=np.int32)

    for i in range(max_iter):
        mask = np.abs(z) <= 2
        julia += mask
        z[mask] = z[mask] ** 2 + (c_real + c_imag * 1j)

    return julia

def create_julia_plot(width, height, c_real, c_imag, max_iter=100):
    julia = julia_set(width, height, c_real, c_imag, max_iter)

    fig = go.Figure(data=go.Heatmap(z=julia, x=np.linspace(-2.0, 2.0, width), y=np.linspace(-2.0, 2.0, height),
                                    colorscale='Viridis', zmin=0, zmax=max_iter))
    fig.update_layout(title=f'Julia Set (c = {c_real} + {c_imag}i)',
                      xaxis_title='Re(z)', yaxis_title='Im(z)',
                      autosize=False, width=900, height=700)
    fig.show()

# Set the width, height, maximum number of iterations, and initial values of c for the Julia Set
width = 1000
height = 1000
max_iter = 1000
c_real = -0.7
c_imag = 0.27015
create_julia_plot(width, height, c_real, c_imag, max_iter)
