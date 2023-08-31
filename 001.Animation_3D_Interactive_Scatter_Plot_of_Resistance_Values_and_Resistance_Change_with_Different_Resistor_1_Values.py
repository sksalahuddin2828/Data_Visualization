import numpy as np
import pandas as pd
import sympy as sp
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from IPython.display import display, HTML

# Problem values
resistors_series = [786, 20.3]
resistors_parallel = [786, 20.3]

# Total resistance for series
total_resistance_series = sum(resistors_series)

# Total resistance for parallel
total_resistance_parallel = 1 / sum(1 / r for r in resistors_parallel)

print("Total Resistance (Series):", total_resistance_series)
print("Total Resistance (Parallel):", total_resistance_parallel)

# Create DataFrame for scatter plot
data = pd.DataFrame({'Resistor 1': np.linspace(1, 1000, 100),
                     'Resistor 2': np.linspace(1, 100, 100)})

# Calculate total resistance for each combination
data['Total Resistance'] = 1 / (1 / data['Resistor 1'] + 1 / data['Resistor 2'])

# Create interactive scatter plot
scatter_plot = px.scatter(data, x='Resistor 1', y='Resistor 2',
                          size='Total Resistance', color='Total Resistance',
                          title='Interactive Scatter Plot of Resistance Values')
scatter_plot.update_layout(coloraxis_colorbar=dict(title='Total Resistance'))
scatter_plot.show()

# Create DataFrame for animated bar chart
resistor_values = np.arange(1, 1001, 50)
resistance_changes = [1 / (1 / resistor + 1 / 20.3) for resistor in resistor_values]

animation_fig = go.Figure(
    data=[go.Bar(x=resistor_values, y=resistance_changes)],
    layout=go.Layout(
        title='Resistance Change with Different Resistor 1 Values',
        xaxis=dict(title='Resistor 1'),
        yaxis=dict(title='Total Resistance'),
        updatemenus=[
            {
                'buttons': [
                    {
                        'args': [None, {'frame': {'duration': 500, 'redraw': True}, 'fromcurrent': True}],
                        'label': 'Play',
                        'method': 'animate',
                    },
                    {
                        'args': [[None], {'frame': {'duration': 0, 'redraw': True}, 'mode': 'immediate', 'transition': {'duration': 0}}],
                        'label': 'Pause',
                        'method': 'animate',
                    },
                ],
                'direction': 'left',
                'pad': {'r': 10, 't': 87},
                'showactive': False,
                'type': 'buttons',
                'x': 0.1,
                'xanchor': 'right',
                'y': 0,
                'yanchor': 'top',
            }
        ],
        sliders=[{
            'active': 0,
            'yanchor': 'top',
            'xanchor': 'left',
            'currentvalue': {
                'font': {'size': 20},
                'prefix': 'Resistor 1:',
                'visible': True,
                'xanchor': 'right',
            },
            'transition': {'duration': 300, 'easing': 'cubic-in-out'},
            'pad': {'b': 10, 't': 50},
            'len': 0.9,
            'x': 0.1,
            'y': 0,
        }],
    ),
    frames=[
        go.Frame(
            data=[go.Bar(x=resistor_values[:idx], y=resistance_changes[:idx])],
            name=str(resistor_value),
        )
        for idx, resistor_value in enumerate(resistor_values)
    ]
)

display(HTML(animation_fig.to_html()))
