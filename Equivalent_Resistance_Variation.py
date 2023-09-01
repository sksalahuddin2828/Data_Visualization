import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from IPython.display import display

# Given resistor values
resistor_values = [36.0, 50.0]

# Create a range of values for Resistor 1 and Resistor 2
resistor1_range = np.linspace(1, 1000, 50)
resistor2_range = np.linspace(1, 1000, 50)

# Create a meshgrid for Resistor 1 and Resistor 2
resistor1_mesh, resistor2_mesh = np.meshgrid(resistor1_range, resistor2_range)

# Calculate the equivalent resistance for each combination
equivalent_resistances = 1 / (1 / resistor1_mesh + 1 / resistor2_mesh)

# Create a DataFrame for the results
data = pd.DataFrame({
    'Resistor 1 (ohms)': resistor1_mesh.flatten(),
    'Resistor 2 (ohms)': resistor2_mesh.flatten(),
    'Equivalent Resistance (ohms)': equivalent_resistances.flatten()
})

# Create an interactive 3D scatter plot using Plotly
fig = go.Figure(data=[go.Scatter3d(
    x=data['Resistor 1 (ohms)'],
    y=data['Resistor 2 (ohms)'],
    z=data['Equivalent Resistance (ohms)'],
    mode='markers',
    marker=dict(
        size=5,
        color=data['Equivalent Resistance (ohms)'],
        colorscale='Viridis',
        opacity=0.7
    ),
)])

fig.update_layout(
    scene=dict(
        xaxis_title='Resistor 1 (ohms)',
        yaxis_title='Resistor 2 (ohms)',
        zaxis_title='Equivalent Resistance (ohms)',
    ),
    title='Equivalent Resistance Variation',
)

display(fig)
