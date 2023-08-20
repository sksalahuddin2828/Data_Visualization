import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import ipywidgets as widgets
from IPython.display import display

# Define symbolic variables
x, a = symbols('x a')

# Define the expression and integrate
expression = x * exp(a * x)
integral_result = (1 / a**2) * (a * x - 1) * exp(a * x)

# Initialize interactive slider
a_slider = widgets.FloatSlider(value=0.1, min=0.1, max=2.0, step=0.1, description='a')
display(a_slider)

# Define x values for plotting
x_values = np.linspace(0, 2, 400)

# Create a pandas DataFrame for data management
data = pd.DataFrame(columns=['x', 'Original Function', 'Integrated Result'])

# Initialize Plotly figure with subplots
fig = make_subplots(rows=1, cols=2, subplot_titles=['Original Function', 'Integrated Result'])

# Define update function for slider
def update_figure(change):
    a_val = a_slider.value
    
    # Calculate original and integrated functions
    original_y = x_values * np.exp(a_val * x_values)
    integrated_y = (np.exp(a_val * x_values) / (a_val**2)) * (a_val * x_values - 1)
    
    # Update DataFrame
    data['x'] = x_values
    data['Original Function'] = original_y
    data['Integrated Result'] = integrated_y
    
    # Clear previous traces
    fig.data = []
    
    # Add traces to Plotly figure
    fig.add_trace(go.Scatter(x=x_values, y=original_y, name='Original Function'), row=1, col=1)
    fig.add_trace(go.Scatter(x=x_values, y=integrated_y, name='Integrated Result'), row=1, col=2)

    # Update subplot titles
    fig.update_xaxes(title_text='x', row=1, col=1)
    fig.update_xaxes(title_text='x', row=1, col=2)
    fig.update_yaxes(title_text='y', row=1, col=1)
    fig.update_yaxes(title_text='y', row=1, col=2)

    # Show the Plotly figure
    fig.show()

# Connect slider to the update function
a_slider.observe(update_figure, names='value')

# Update layout for Plotly figure
fig.update_layout(title_text='Integration of x * e^(a * x)')

# Display the initial Plotly figure
fig.show()

# Display the data DataFrame
data
