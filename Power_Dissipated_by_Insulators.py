import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Given data
voltage = 240e3  # Volts
resistance_per_insulator = 1.00e9  # Ohms
number_of_insulators = 100
power_transmitted = 5.00e2  # Watts

# Problem (a)
total_resistance = 1 / np.sum(1 / resistance_per_insulator)

# Problem (b)
current = voltage / total_resistance
power_dissipated = current ** 2 * total_resistance

# Problem (c)
fraction_dissipated = power_dissipated / power_transmitted

# Create a DataFrame for visualization
data = {
    "Number of Insulators": np.arange(1, 101),
    "Total Resistance (Ohms)": [1 / (1 / resistance_per_insulator * n) for n in range(1, 101)],
}
df = pd.DataFrame(data)

# Visualize the resistance of insulators
fig1 = px.line(df, x="Number of Insulators", y="Total Resistance (Ohms)", title="Resistance of Insulators in Parallel")
fig1.update_xaxes(title_text="Number of Insulators")
fig1.update_yaxes(title_text="Total Resistance (Ohms)")

# Visualize power dissipation
fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=[number_of_insulators], y=[power_dissipated],
                          mode="markers", name="Power Dissipated", marker=dict(size=10)))
fig2.update_layout(title="Power Dissipated by Insulators",
                   xaxis_title="Number of Insulators",
                   yaxis_title="Power Dissipated (Watts)")

# Print results
print("Total resistance to ground:", total_resistance, "Ohms")
print("Power dissipated:", power_dissipated, "Watts")
print("Fraction of power dissipated:", fraction_dissipated)

# Display visualizations
fig1.show()
fig2.show()
