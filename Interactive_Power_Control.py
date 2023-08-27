from bokeh.layouts import column
from bokeh.models import Slider, ColumnDataSource
from bokeh.plotting import curdoc, figure
import numpy as np

# Create a ColumnDataSource for the data
source = ColumnDataSource(data=dict(time=[], cost=[]))

# Given values
power = 50.0  # kW
electricity_cost = 0.09  # cents/kWh

# Create a figure
p = figure(title="Interactive Power Control", x_axis_label="Time (hours)", y_axis_label="Cost (USD)")

# Plot the cost curve
time_range = np.arange(0, 24, 0.5)
costs = time_range * power * electricity_cost
p.line(time_range, costs, line_width=2, legend_label="Cost")

# Add selected time marker
selected_time_marker = p.circle('time', 'cost', source=source, size=10, color='red', legend_label="Selected Time")

# Define callback function for slider
def update(attrname, old, new):
    selected_time = slider.value
    selected_cost = selected_time * power * electricity_cost
    source.data = dict(time=[selected_time], cost=[selected_cost])

# Create a slider
slider = Slider(start=0, end=24, value=8, step=1, title="Select Time (hours)")
slider.on_change('value', update)

# Set up layout
layout = column(p, slider)

# Add layout to current document
curdoc().add_root(layout)
