import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Constants
battery_voltages = [1.58, 1.58, 1.58, 1.53]  # Voltages of alkaline cells and carbon-zinc dry cell (in V)
battery_internal_resistances = [0.0200, 0.0200, 0.0200, 0.100]  # Internal resistances (in ohms)
load_resistance = 10.0  # Load resistance (in ohms)

# Total voltage across the batteries with internal resistances
total_voltage = sum(battery_voltages) - sum(battery_internal_resistances)

# Calculate current using Ohm's law
total_resistance = sum(battery_internal_resistances) + load_resistance
current = total_voltage / total_resistance

# Calculate power supplied to the load
power_supplied = current * total_voltage

# Internal resistance calculation using optimization (e.g., scipy)
from scipy.optimize import minimize_scalar

def power_difference(internal_resistance):
    total_v = sum(battery_voltages) - internal_resistance * len(battery_voltages)
    total_r = sum(battery_internal_resistances) + load_resistance + internal_resistance * len(battery_voltages)
    current = total_v / total_r
    power = current * total_v
    return abs(power - 0.5)  # Difference from the desired power

result = minimize_scalar(power_difference)
internal_resistance_dry_cell = result.x

# Create DataFrames for components and their properties
components = ["Alkaline Cell 1", "Alkaline Cell 2", "Alkaline Cell 3", "Dry Cell", "Load"]
voltages = battery_voltages + [0] + [total_voltage]
internal_resistances = battery_internal_resistances + [internal_resistance_dry_cell] + [load_resistance]

df_components = pd.DataFrame({"Component": components})
df_voltages = pd.DataFrame({"Voltage (V)": voltages})
df_resistances = pd.DataFrame({"Internal Resistance (Ω)": internal_resistances})

# Concatenate the DataFrames
df_properties = pd.concat([df_components, df_voltages, df_resistances], axis=1)

# Visualization using Plotly
# Circuit diagram (create your artistic representation here)
circuit_diagram = go.Figure()
circuit_diagram.update_layout(
    title_text="Circuit Diagram",
    title_x=0.5,
    showlegend=False,
    xaxis=dict(visible=False),
    yaxis=dict(visible=False),
)
# Add your artistic representation here using annotations or shapes

# Bar chart for component values
component_fig = px.bar(
    df_properties,
    x="Component",
    y=["Voltage (V)", "Internal Resistance (Ω)"],
    title="Component Voltages and Internal Resistances",
    labels={"value": "Value"},
)

# Pie chart to show the proportion of each battery's voltage
battery_labels = [f"Battery {i + 1}" for i in range(len(battery_voltages))]
battery_fig = px.pie(
    values=battery_voltages,
    names=battery_labels,
    title="Proportion of Battery Voltages",
)

# Document your project using Pandas and include explanations
# For example, you can add a LaTeX-formatted explanation of Ohm's law and power calculations.

# Display the visualizations
circuit_diagram.show()
component_fig.show()
battery_fig.show()

# Output internal resistance calculation result
print(f"Internal Resistance of Dry Cell: {internal_resistance_dry_cell:.4f} ohms")
