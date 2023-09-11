import numpy as np
import pandas as pd
import plotly.graph_objects as go

# Given values
C = 8.00e-6  # Capacitance (F)
R = 1.00e3   # Resistance (Ω)
V_initial = 10.0e3  # Initial voltage (V)
V_final = 5.00e2    # Final voltage (V)

# Part (a) - Calculate the time constant (τ)
tau = R * C

# Part (b) - Calculate the time it takes to decline to V_final
t = -tau * np.log(V_final / V_initial)

# Create a DataFrame for the voltage decay over time
time_values = np.linspace(0, 3 * tau, 1000)  # Time values
voltage_values = V_initial * np.exp(-time_values / tau)  # Voltage values
df = pd.DataFrame({'Time (s)': time_values, 'Voltage (V)': voltage_values})

# Create a line plot using Plotly
fig = go.Figure()
fig.add_trace(go.Scatter(x=df['Time (s)'], y=df['Voltage (V)'],
                         mode='lines', name='Voltage Decay'))
fig.update_layout(title='Capacitor Discharge Over Time',
                  xaxis_title='Time (s)', yaxis_title='Voltage (V)')

# Print results
print(f"(a) Time Constant (τ): {tau:.4f} seconds")
print(f"(b) Time to Decline to {V_final} V: {t:.4f} seconds")

# Show the interactive Plotly plot
fig.show()
