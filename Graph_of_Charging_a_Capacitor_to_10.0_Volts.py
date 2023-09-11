import numpy as np
import pandas as pd
import plotly.express as px

# Define capacitor parameters
C = 1.0  # Capacitance (in Farads)
R = 1.0  # Resistance (in Ohms)
V_emf = 10.0  # EMF (in Volts)

# Define the voltage function during charging
def voltage(t):
    return V_emf * (1 - np.exp(-t / (R * C)))

# Create a time array
t = np.linspace(0, 5 * R * C, 1000)

# Calculate the voltage across the capacitor at each time point
V = voltage(t)

# Create a DataFrame for plotting
df = pd.DataFrame({'Time': t, 'Voltage': V})

# Create an animated line chart using Plotly
fig = px.line(df, x='Time', y='Voltage', title=f'Charging a Capacitor to {V_emf} Volts')

# Configure animation settings
fig.update_traces(line=dict(smoothing=0.85))
fig.update_xaxes(range=[0, t[-1]])
fig.update_yaxes(range=[0, V_emf])
fig.update_layout(
    xaxis_title='Time (seconds)',
    yaxis_title='Voltage (Volts)',
    showlegend=False,  # Hide the legend
    xaxis=dict(showline=True, zeroline=False),
    yaxis=dict(showline=True, zeroline=False)
)

# Add a vertical line to indicate the charging time
charging_time = next((time for time, voltage in zip(t, V) if voltage >= V_emf), None)
if charging_time is not None:
    fig.add_shape(
        dict(
            type="line",
            x0=charging_time,
            x1=charging_time,
            y0=0,
            y1=V_emf,
            line=dict(color="red", width=2),
        )
    )

# Show the animated chart
fig.show()
