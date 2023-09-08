import numpy as np
import sympy as sp
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import ipywidgets as widgets
from IPython.display import display

# Function to calculate parallel resistance
def parallel_resistance(galvanometer_resistance, full_scale_current):
    return galvanometer_resistance / (full_scale_current / 1000) - galvanometer_resistance

# Define symbolic variables for resistance, current, and sensitivity
R, I, S = sp.symbols('R I S')

# Create an equation for parallel resistance
equation = sp.Eq(1 / R, (I / S) - (1 / 10))

# Solve the equation symbolically
solution = sp.solve(equation, R)

# Define current and sensitivity values for plotting
current_values = np.linspace(0.001, 50, 100)  # A
sensitivity_values = np.linspace(0.001, 500, 100)  # μA

# Create a meshgrid for 3D visualization
I, S = np.meshgrid(current_values, sensitivity_values)
R = parallel_resistance(10, I)

# Create a Pandas DataFrame to store the data
data = {'Current (A)': I.flatten(),
        'Sensitivity (μA)': S.flatten(),
        'Resistance (Ω)': R.flatten()}
df = pd.DataFrame(data)

# Create interactive sliders for current and sensitivity
current_slider = widgets.FloatSlider(value=20, min=0.001, max=50, step=0.1, description='Current (A)')
sensitivity_slider = widgets.FloatSlider(value=100, min=0.001, max=500, step=1, description='Sensitivity (μA)')

# Function to update the 3D plot based on slider values
def update_plot(change):
    current = current_slider.value
    sensitivity = sensitivity_slider.value
    updated_R = parallel_resistance(10, current)
    
    # Update the scatter plot and title
    fig.update_traces(z=[updated_R])
    fig.update_layout(title=f'Parallel Resistance vs. Current and Sensitivity (Current={current} A, Sensitivity={sensitivity} μA)')

# Create initial 3D surface plot
fig = px.scatter_3d(df, x='Current (A)', y='Sensitivity (μA)', z='Resistance (Ω)',
                     title='Parallel Resistance vs. Current and Sensitivity',
                     labels={'Resistance (Ω)': 'Resistance (Ω)'})

# Display the 3D plot and sliders
display(fig)
widgets.interactive(update_plot, change=current_slider)
widgets.interactive(update_plot, change=sensitivity_slider)
