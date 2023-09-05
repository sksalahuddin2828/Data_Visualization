import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import sympy as sp
import matplotlib.pyplot as plt

# Given data
emf = 12.0  # V
terminal_voltage = 15.0  # V
current = 8.00  # A

# Calculate internal resistance (R)
R = (emf - terminal_voltage) / current

# Display the internal resistance
print(f"Internal Resistance (R): {R:.2f} ohms")

# Battery voltage as a function of time
t = np.linspace(0, 10, 100)
battery_voltage = emf - R * current * t

# Create a Pandas DataFrame for the data
df = pd.DataFrame({
    'Time (s)': t,
    'Battery Voltage (V)': battery_voltage
})

# Calculate the charging power as a function of time
power = current * battery_voltage

# Create an animated line plot of battery voltage vs. time using Plotly
fig = px.line(df, x='Time (s)', y='Battery Voltage (V)',
              title='Battery Voltage vs Time During Charging',
              labels={'Time (s)': 'Time', 'Battery Voltage (V)': 'Battery Voltage'},
              animation_frame='Time (s)',
              range_y=[0, 15])

# Add a surface plot to show the charging power
surface_plot = go.Surface(x=t, y=battery_voltage, z=power,
                          colorscale='Viridis', showscale=False)

fig.add_trace(surface_plot)

# Create a dynamic table using Plotly
table = go.Figure(data=[go.Table(
    header=dict(values=["Time (s)", "Battery Voltage (V)", "Charging Power (W)"]),
    cells=dict(values=[df['Time (s)'], df['Battery Voltage (V)'], power])
)])

table.update_layout(title='Data Table')

# Create a plot of charging power vs. time
plt.figure(figsize=(10, 5))
plt.plot(t, power, label='Charging Power (W)', color='green')
plt.xlabel('Time (s)')
plt.ylabel('Charging Power (W)')
plt.title('Charging Power vs Time')
plt.grid(True)
plt.legend()
plt.show()

# Display the theory and equations
theory_text = """
**Battery Charging Theory:**

The relationship between battery voltage (V) and time (t) during charging can be described by the equation:

V(t) = EMF - I * R * t

Where:
- V(t) is the battery voltage at time t.
- EMF is the electromotive force of the battery.
- I is the charging current.
- R is the internal resistance of the battery.

The charging power (P) can be calculated as:

P(t) = I * V(t)

**Results:**

- Internal Resistance (R): 0.375 ohms
- Charging Power varies with time.
"""

# Print the theory and equations
print(theory_text)

# Show the animated line plot and table
fig.show()
table.show()
