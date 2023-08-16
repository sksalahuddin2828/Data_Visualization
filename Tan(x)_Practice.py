import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Generate x values
x_vals = np.linspace(-10, 10, 300)
n_terms_vals = [1, 3, 5, 7, 9, 11]  # Number of terms for the series

# Initialize subplots
fig = make_subplots(rows=2, cols=1, shared_xaxes=True,
                    vertical_spacing=0.05, subplot_titles=('Function Comparison', 'Series Approximation'))

# Calculate tan(x) for all x values
tan_x = np.tan(x_vals)

# Plot tan(x)
scatter_tan = go.Scatter(x=x_vals, y=tan_x, mode='lines', name='tan(x)',
                         line=dict(color='blue', width=2))
fig.add_trace(scatter_tan, row=1, col=1)

# Initialize data list for series approximations
series_data = []

# Calculate series approximations for different number of terms
for n_terms in n_terms_vals:
    series_approx = np.sum([(x_val ** (2 * k + 1)) / ((2 * k + 1) * np.math.factorial(2 * k + 1)) for k in range(n_terms)])
    series_data.append(series_approx)

# Plot series approximations
scatter_series = go.Scatter(x=x_vals, y=series_data, mode='lines+markers', name='Series Approximation',
                            line=dict(color='green', width=2),
                            marker=dict(size=8, color='green'))
fig.add_trace(scatter_series, row=2, col=1)

# Update subplot layout
fig.update_xaxes(title_text='x', row=2, col=1)
fig.update_yaxes(title_text='tan(x)', row=1, col=1)
fig.update_yaxes(title_text='Series Approximation', row=2, col=1)

# Add animation slider
steps = []
for i, n_terms in enumerate(n_terms_vals):
    step = dict(args=[{"y": [tan_x, series_data[i]]},
                      {"yaxis.title.text": "Function"}],
                label=f"{n_terms} terms",
                method="update")
    steps.append(step)

sliders = [dict(steps=steps, active=0, currentvalue={"prefix": "Number of terms: "})]

# Update layout for animation
fig.update_layout(updatemenus=[dict(type='buttons', showactive=False, buttons=[dict(label='Play',
                                                                                   method='animate',
                                                                                   args=[None, {"frame": {"duration": 1000, "redraw": True},
                                                                                                 "fromcurrent": True, "transition": {"duration": 300, "easing": 'quadratic-in-out'}}])])],
                  sliders=sliders, title_text='Tan(x) vs. Series Approximation with Terms Animation')

# Show the plot
fig.show()
