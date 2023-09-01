import numpy as np
import sympy as sp
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import ipywidgets as widgets
from IPython.display import display, Math

# Given resistor values
resistor_values = [36.0, 50.0, 700.0]

# Create a DataFrame for the results
data = pd.DataFrame(columns=['Resistor 1 (ohms)', 'Resistor 2 (ohms)', 'Equivalent Resistance (ohms)'])

# Calculate all possible combinations of resistor values and update the DataFrame
for i in range(2**len(resistor_values)):
    combination = []
    for j in range(len(resistor_values)):
        if (i >> j) & 1:
            combination.append(resistor_values[j])
    if len(combination) == len(resistor_values):  # Check if all resistors are used
        equivalent_resistance = np.sum(1 / np.array(combination))
        data = data.append({
            'Resistor 1 (ohms)': combination[0],
            'Resistor 2 (ohms)': combination[1],
            'Equivalent Resistance (ohms)': equivalent_resistance
        }, ignore_index=True)

# Create an interactive 3D scatter plot using Plotly
fig = px.scatter_3d(data, x='Resistor 1 (ohms)', y='Resistor 2 (ohms)', z='Equivalent Resistance (ohms)',
                    color='Equivalent Resistance (ohms)', opacity=0.7, title='Equivalent Resistance Combinations',
                    labels={'Equivalent Resistance (ohms)': 'Equivalent Resistance (ohms)'})
fig.update_layout(scene=dict(xaxis_title='Resistor 1 (ohms)', yaxis_title='Resistor 2 (ohms)',
                             zaxis_title='Equivalent Resistance (ohms)'))

# Add custom labels to data points
custom_labels = []
for index, row in data.iterrows():
    custom_labels.append(f"R1: {row['Resistor 1 (ohms)']} ohms<br>R2: {row['Resistor 2 (ohms)']} ohms<br>Requiv: {row['Equivalent Resistance (ohms)']} ohms")
fig.update_traces(text=custom_labels, selector=dict(mode='markers'))

# Create a mathematical explanation
math_explanation = widgets.Output()
with math_explanation:
    display(Math(r'R_{\text{eq}} = \frac{1}{\frac{1}{R_1} + \frac{1}{R_2}}'))

# Create an interactive input widget
resistor1_input = widgets.FloatSlider(value=36.0, min=1, max=1000, step=1, description='Resistor 1 (ohms)')
resistor2_input = widgets.FloatSlider(value=50.0, min=1, max=1000, step=1, description='Resistor 2 (ohms)')
interactive_output = widgets.Output()

# Update the output when the user changes the resistor values
def update_output(change):
    with interactive_output:
        equivalent_resistance = 1 / (1 / resistor1_input.value + 1 / resistor2_input.value)
        print(f"Equivalent Resistance: {equivalent_resistance} ohms")

resistor1_input.observe(update_output, 'value')
resistor2_input.observe(update_output, 'value')

# Display the widgets
display(math_explanation)
display(resistor1_input)
display(resistor2_input)
display(interactive_output)
fig.show()
