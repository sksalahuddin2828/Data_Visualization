import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import sympy as sp
import matplotlib.pyplot as plt

# Given data
Rx = 1.200  # Ohms
Rs = 1.247  # Ohms
standard_cell_emf = 1.600  # Volts

# Calculate the EMF of the dry cell using the potentiometer equation
emf_dry_cell = standard_cell_emf * (Rx / Rs)

# Create a pandas DataFrame for the results
data = {'Rx (Ω)': [Rx], 'Rs (Ω)': [Rs], 'EMF Dry Cell (V)': [emf_dry_cell]}
df = pd.DataFrame(data)

# Print the result
print(df)

# Create a 3D scatter plot using Plotly
fig = px.scatter_3d(df, x='Rx (Ω)', y='Rs (Ω)', z='EMF Dry Cell (V)',
                     title='EMF Calculation for Dry Cell',
                     labels={'EMF Dry Cell (V)': 'EMF Dry Cell (V)'})
fig.update_traces(marker=dict(size=5))  # Customize marker size

# Add a surface plot to visualize the EMF calculation surface
rx_values = np.linspace(1.0, 2.0, 100)
rs_values = np.linspace(1.0, 2.0, 100)
rx_mesh, rs_mesh = np.meshgrid(rx_values, rs_values)
emf_mesh = standard_cell_emf * (rx_mesh / rs_mesh)

fig.add_trace(go.Surface(z=emf_mesh, x=rx_mesh, y=rs_mesh, colorscale='Viridis', opacity=0.7))

# Add an interactive slider to control the standard cell EMF
fig.update_layout(
    sliders=[{
        "steps": [
            {"args": ["slider.value", 1.0], "label": "1.0 V", "method": "animate"},
            {"args": ["slider.value", 1.5], "label": "1.5 V", "method": "animate"},
            {"args": ["slider.value", 2.0], "label": "2.0 V", "method": "animate"}
        ],
        "active": 0,
        "yanchor": "top",
        "xanchor": "left",
        "currentvalue": {
            "prefix": "Standard Cell EMF: ",
            "suffix": " V",
            "visible": True,
            "xanchor": "left"
        },
        "transition": {"duration": 300, "easing": "cubic-in-out"}
    }]
)

# Show the interactive plot
fig.show()

# Create a 2D scatter plot of the calculated EMF vs. Rs
rs_values = np.linspace(1.0, 2.0, 100)
emf_values = standard_cell_emf * (Rx / rs_values)
plt.figure(figsize=(10, 6))
plt.scatter(rs_values, emf_values, c='b', label=f'Rx = {Rx} Ω', marker='o')
plt.xlabel('Rs (Ω)')
plt.ylabel('EMF Dry Cell (V)')
plt.title('EMF vs. Rs for a Dry Cell')
plt.legend()
plt.grid(True)

# Show the 2D plot
plt.show()
