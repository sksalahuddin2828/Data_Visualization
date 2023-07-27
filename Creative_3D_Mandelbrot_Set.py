import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def mandelbrot_set(width, height, max_iter=100):
    x_min, x_max = -2.5, 1.5
    y_min, y_max = -1.5, 1.5
    x, y = np.linspace(x_min, x_max, width), np.linspace(y_min, y_max, height)
    X, Y = np.meshgrid(x, y)
    c = X + 1j * Y
    z = np.zeros_like(c, dtype=np.complex128)
    mandelbrot = np.zeros_like(c, dtype=np.int32)

    for i in range(max_iter):
        mask = np.abs(z) <= 2
        mandelbrot += mask
        z[mask] = z[mask] ** 2 + c[mask]

    return mandelbrot

def create_mandelbrot_plot(width, height, max_iter=100):
    mandelbrot = mandelbrot_set(width, height, max_iter)

    fig = go.Figure(data=go.Contour(z=mandelbrot, x=np.linspace(-2.5, 1.5, width), y=np.linspace(-1.5, 1.5, height),
                                    contours=dict(start=0, end=max_iter, size=1, coloring='heatmap')))
    fig.update_layout(title='Mandelbrot Set',
                      xaxis_title='Re(c)', yaxis_title='Im(c)',
                      autosize=False, width=900, height=700)
    fig.show()

# Set the width, height, and maximum number of iterations for the Mandelbrot Set
width = 1000
height = 1000
max_iter = 1000
create_mandelbrot_plot(width, height, max_iter)
