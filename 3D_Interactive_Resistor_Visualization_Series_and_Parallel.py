import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

# Define resistor values and configuration (you can extend this for more resistors)
resistors = pd.DataFrame({'Resistance (Ohms)': [10, 20],
                          'Configuration': ['Series', 'Parallel']})

# Create a DataFrame to hold resistor positions
positions = pd.DataFrame({'X': [0, 30], 'Y': [0, 0], 'Z': [0, 0]})

# Create a 3D scatter plot using Plotly
fig = px.scatter_3d(resistors, x=positions['X'], y=positions['Y'], z=positions['Z'],
                     color='Configuration', text='Resistance (Ohms)', opacity=0.7,
                     title='Interactive Resistor Visualization')

# Customize the layout
fig.update_layout(scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Z'),
                  showlegend=True)

# Add resistor values as text labels
for i in range(len(resistors)):
    fig.add_trace(go.Scatter3d(x=[positions['X'][i]], y=[positions['Y'][i]], z=[positions['Z'][i]],
                               text=[f'Resistance: {resistors["Resistance (Ohms)"][i]} Ohms'],
                               mode='text'))

# Show the interactive plot
fig.show()
