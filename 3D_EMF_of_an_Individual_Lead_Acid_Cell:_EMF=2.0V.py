import numpy as np
import pandas as pd
import plotly.graph_objs as go

# Constants
total_emf = 12.0  # Total EMF of the automobile battery in volts
num_cells = 6    # Number of lead-acid cells in series

# Calculate the EMF of an individual cell
emf_individual_cell = total_emf / num_cells

# Create a DataFrame to store data points for visualization
resistance_range = np.linspace(0, 1, 100)
voltage_drop_range = np.linspace(0, 1, 100)
resistance, voltage_drop = np.meshgrid(resistance_range, voltage_drop_range)
emf_values = emf_individual_cell - resistance * emf_individual_cell - voltage_drop * emf_individual_cell

df = pd.DataFrame({'Resistance': resistance.flatten(),
                   'Voltage Drop': voltage_drop.flatten(),
                   'EMF': emf_values.flatten()})

# Create frames for the animation
frames = [go.Frame(data=[go.Scatter3d(x=df['Resistance'], y=df['Voltage Drop'], z=df['EMF'],
                                      mode='markers',
                                      marker=dict(size=5, color=df['EMF'], colorscale='Viridis'))],
                   name=f'Frame {i+1}')
          for i in range(10)]  # You can adjust the number of frames and animation speed

# Create the animation
animation = [go.Scatter3d(x=df['Resistance'], y=df['Voltage Drop'], z=df['EMF'],
                          mode='markers',
                          marker=dict(size=5, color=df['EMF'], colorscale='Viridis'))]

# Create the layout with updatemenus for animation
layout = go.Layout(
    title=f'EMF of an Individual Lead-Acid Cell: EMF = {emf_individual_cell} V',
    scene=dict(
        xaxis_title='Cell Resistance',
        yaxis_title='Internal Voltage Drop',
        zaxis_title='EMF (V)',
    ),
    updatemenus=[
        {
            'buttons': [
                {
                    'args': [None, {'frame': {'duration': 1000, 'redraw': True}, 'fromcurrent': True}],
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
        },
    ],
)

# Create a list to store the slider configuration
slider_steps = []

# Populate the steps for the animation
for i in range(10):
    step = {
        'args': [
            [f'Frame {i+1}'],
            {
                'frame': {'duration': 1000, 'redraw': True},
                'mode': 'immediate',
                'transition': {'duration': 1000},
            },
        ],
        'label': f'Frame {i+1}',
        'method': 'animate',
    }
    slider_steps.append(step)

# Add the slider configuration to the buttons in updatemenus
layout.updatemenus[0]['buttons'][0]['args'][1]['frame']['duration'] = 1000  # Set animation speed
layout.updatemenus[0]['buttons'][0]['args'][1]['steps'] = slider_steps

# Create the figure
fig = go.Figure(data=animation, layout=layout, frames=frames)

# Show the animated plot
fig.show()
