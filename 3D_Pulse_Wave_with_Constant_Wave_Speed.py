from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
from bokeh.layouts import column
from bokeh.io import push_notebook, output_notebook
from ipywidgets import interact
import numpy as np

output_notebook()

def pulse_wave(x, A, v):
    return A * np.exp(-x/v)

x_values = np.linspace(0, 10, 100)
A = 1.0  # Amplitude
v = 2.0  # Wave speed

p = figure(title='Pulse Wave with Constant Wave Speed', x_axis_label='x (m)', y_axis_label='Amplitude',
           width=800, height=400)

source = ColumnDataSource(data={'x': x_values, 'y': pulse_wave(x_values, A, v)})
p.line('x', 'y', source=source, line_width=2)

def update_pulse_wave(amplitude, wave_speed):
    new_y = pulse_wave(x_values, amplitude, wave_speed)
    source.data = {'x': x_values, 'y': new_y}
    push_notebook()

show(column(p), notebook_handle=True)

interact(update_pulse_wave, amplitude=(0.1, 2.0, 0.1), wave_speed=(0.1, 5.0, 0.1))
