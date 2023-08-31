import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Generate data
R1_values = np.linspace(1, 1000, 50)
R2_values = np.linspace(1, 100, 50)

R1, R2 = np.meshgrid(R1_values, R2_values)
series_resistances = R1 + R2
parallel_resistances = 1 / (1 / R1 + 1 / R2)

# Create DataFrame for Series and Parallel Resistance
df = pd.DataFrame({'R1': R1.flatten(), 'R2': R2.flatten(),
                   'Series Resistance': series_resistances.flatten(),
                   'Parallel Resistance': parallel_resistances.flatten()})

# Create interactive scatter plots
fig = px.scatter(df, x='R1', y='R2', size='Series Resistance', color='Series Resistance',
                 hover_name='Series Resistance', labels={'Series Resistance': 'Series Resistance'},
                 title='Series and Parallel Resistance Visualization')

# Add mathematical expressions to the hover text
fig.update_traces(texttemplate="Series Resistance: %{hovertext:.2f} Ω<br>R1: %{x:.2f} Ω<br>R2: %{y:.2f} Ω",
                  hovertext=df['Series Resistance'])

# Create parallel resistance curves
parallel_curve = go.Scatter(x=df['R1'], y=df['R2'], mode='lines', line=dict(width=2, color='red'),
                            name='Parallel Resistance Curve', showlegend=True)
fig.add_trace(parallel_curve)

# Add animation to show parallel resistance curve
frames = [go.Frame(data=[go.Scatter(x=df['R1'], y=df['R2'], mode='lines',
                                    line=dict(width=2, color='red')),
                         go.Scatter(x=[r1], y=[r2], mode='markers',
                                    marker=dict(size=10, color='black'), name='Current Selection')],
                   name=f"R1: {r1} Ω, R2: {r2} Ω")
          for r1, r2 in zip(df['R1'], df['R2'])]

fig.frames = frames

# Update animation settings
fig.update_layout(updatemenus=[{'type': 'buttons', 'showactive': False,
                                 'buttons': [{'label': 'Play',
                                              'method': 'animate',
                                              'args': [None, {'frame': {'duration': 500, 'redraw': True}, 'fromcurrent': True}]
                                             }]
                                }]
                 )

# Display plot
fig.show()
