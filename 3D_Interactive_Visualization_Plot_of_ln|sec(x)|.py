import numpy as np
import plotly.graph_objects as go

x_vals = np.linspace(-2*np.pi, 2*np.pi, 400)
y_vals = np.log(np.abs(1/np.cos(x_vals)))

fig = go.Figure(data=go.Scatter(x=x_vals, y=y_vals, mode='lines'))
fig.update_layout(title='Interactive Visualization of ln|sec(x)|',
                  xaxis_title='x', yaxis_title='ln|sec(x)|')

fig.show()
