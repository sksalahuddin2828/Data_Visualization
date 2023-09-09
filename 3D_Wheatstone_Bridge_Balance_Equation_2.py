import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import sympy as sp

# Define the symbols
Rx, R1, R2, R3 = sp.symbols('Rx R1 R2 R3')

# Given ratio R2/R1
ratio = 0.625

# Balance equation for the Wheatstone bridge
balance_equation = sp.Eq(R2 / R1, (R3 / Rx))

# Create a DataFrame to store the results
results_df = pd.DataFrame(columns=['R1', 'R2', 'R3', 'Rx'])

# Generate a range of values for R1 and R2
R1_values = np.linspace(1, 1000, 100)
R2_values = R1_values * ratio

# Create an empty list to store scatter traces
scatter_traces = []

# Iterate through R1 and R2 values
for R1_val, R2_val in zip(R1_values, R2_values):
    # Solve for Rx
    solution = sp.solve(balance_equation.subs({R1: R1_val, R2: R2_val, R3: 2500}), Rx)
    Rx_val = float(solution[0])  # Convert to float
    
    # Add data to the DataFrame
    results_df = results_df.append({'R1': R1_val, 'R2': R2_val, 'R3': 2500, 'Rx': Rx_val}, ignore_index=True)
    
    # Create a scatter plot for each data point
    scatter_trace = go.Scatter3d(x=[R1_val], y=[R2_val], z=[Rx_val], mode='markers', marker=dict(size=5))
    
    scatter_traces.append(scatter_trace)

# Create an initial figure with the first scatter trace
fig = go.Figure(data=[scatter_traces[0]])

# Define the frames for animation
frames = [go.Frame(data=[trace], name=f'Frame {i}') for i, trace in enumerate(scatter_traces)]

# Customize the layout
fig.update_layout(
    scene=dict(
        xaxis_title='R1',
        yaxis_title='R2',
        zaxis_title='Rx',
    ),
    title="Wheatstone Bridge Balance Equation",
)

# Add animation settings
fig.frames = frames

# Display the interactive plot using Plotly
fig.show()

# Display the DataFrame
print("Results:")
print(results_df)
