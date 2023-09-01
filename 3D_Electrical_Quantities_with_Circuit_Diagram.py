import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Given values
V = 12.0  # Voltage (in volts)
R1 = 1.00  # Resistance of R1 (in ohms)
R2 = 6.00  # Resistance of R2 (in ohms)
R3 = 13.00  # Resistance of R3 (in ohms)

# Step 1: Calculate the equivalent resistance (R_eq) for the parallel combination of R2 and R3
R_eq = 1 / (1 / R2 + 1 / R3)

# Step 2: Calculate the total resistance (R_total) for the circuit
R_total = R1 + R_eq

# Step 3: Calculate the total current (I) using Ohm's law
I = V / R_total

# Step 4: Calculate I2 using the current divider rule
I2 = I * (R3 / (R2 + R3))

# Step 5 (a): Calculate I3 using known values of I and I2
I3_a = I - I2

# Step 5 (b): Calculate I3 using Ohm's law for R3
I3_b = V / R3

# Calculate power P3
P3 = I3_b ** 2 * R3

# Calculate total power supplied by the source
P_total_source = V * I

# Calculate the sum of powers dissipated by the resistors
P_total_resistors = V ** 2 / R_total

# Create a pandas DataFrame to present the results
data = {
    "Quantity": ["R_eq", "R_total", "I", "I2", "I3 (Method a)", "I3 (Method b)", "P3", "P_total_source", "P_total_resistors"],
    "Value": [R_eq, R_total, I, I2, I3_a, I3_b, P3, P_total_source, P_total_resistors],
}
df = pd.DataFrame(data)

# Display the DataFrame
print(df)

# Create an interactive 3D scatter plot using Plotly
fig = px.scatter_3d(df, x='Value', y='Value', z='Value', text='Quantity')
fig.update_traces(marker=dict(size=5, opacity=0.6), selector=dict(mode='markers+text'))

fig.update_layout(
    scene=dict(
        xaxis_title='Value',
        yaxis_title='Value',
        zaxis_title='Value',
        camera_eye=dict(x=1.2, y=1.2, z=1.2),
    ),
    title="Interactive 3D Scatter Plot of Electrical Quantities",
)

# Create a circuit diagram using Pandas DataFrame (creative representation)
circuit_df = pd.DataFrame({
    "Component": ["Battery", "R1", "Parallel (R2 and R3)"],
    "Value": [f"{V} V", f"{R1} Ω", f"{R2} Ω || {R3} Ω"]
})

# Create a table representing the circuit
table = go.Figure(data=[go.Table(
    header=dict(values=['Component', 'Value']),
    cells=dict(values=[circuit_df['Component'], circuit_df['Value']]))
])

table.update_layout(
    title="Creative Circuit Diagram",
    margin=dict(l=0, r=0, t=50, b=0),
)

# Show the interactive 3D plot and circuit diagram
fig.show()
table.show()
