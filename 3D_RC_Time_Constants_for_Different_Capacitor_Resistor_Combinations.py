import numpy as np
import pandas as pd
import plotly.express as px

# Capacitor and resistor values
capacitors = [2.00e-6, 7.50e-6]
resistors = [25.0e3, 100.0e3]

# Initialize an empty DataFrame to store data
data = pd.DataFrame(columns=["Resistance (Ohms)", "Capacitance (Farads)", "RC Time Constant (s)"])

# Calculate RC time constants for all possible combinations
for C in capacitors:
    for R in resistors:
        time_constant = R * C
        data = data.append({"Resistance (Ohms)": R, "Capacitance (Farads)": C, "RC Time Constant (s)": time_constant}, ignore_index=True)

# Create an interactive 3D scatter plot using Plotly
fig = px.scatter_3d(data, x="Resistance (Ohms)", y="Capacitance (Farads)", z="RC Time Constant (s)", color="RC Time Constant (s)",
                    labels={"RC Time Constant (s)": "RC Time Constant (s)"})
fig.update_layout(scene=dict(xaxis_title='Resistance (Ohms)', yaxis_title='Capacitance (Farads)'))
fig.update_layout(title='RC Time Constants for Different Capacitor-Resistor Combinations')
fig.show()
