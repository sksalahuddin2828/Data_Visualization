import numpy as np
import pandas as pd
import plotly.express as px

# Define parameters
R = 1000  # Ohms
C = 0.001  # Farads
V0 = 10  # Initial voltage (e.g., 10 volts)
tau = R * C  # Time constant

# Create time values
time = np.linspace(0, 5 * tau, 1000)  # Adjust the time range as needed

# Calculate potential difference across the resistor
V_resistor = V0 * np.exp(-time / tau)

# Calculate current
current = V_resistor / R

# Create a DataFrame for easy data manipulation
data = pd.DataFrame({'Time': time, 'Potential Difference (V)': V_resistor, 'Current (A)': current})

# Create an interactive line plot using Plotly Express
fig = px.line(data, x='Time', y=['Potential Difference (V)', 'Current (A)'],
              labels={'Time': 'Time (s)', 'value': 'Value'},
              title='Potential Difference and Current vs. Time',
              line_shape='linear', render_mode='auto')

# Customize the plot layout and appearance
fig.update_layout(
    xaxis=dict(showline=True, title_font=dict(size=16)),
    yaxis=dict(showline=True, title_font=dict(size=16)),
    legend=dict(x=0.1, y=0.9),
    font=dict(size=14),
    template="plotly_dark"
)

# Add vertical lines to indicate two intervals of τ
fig.add_shape(
    dict(type='line', x0=0.5 * tau, x1=0.5 * tau, y0=0, y1=max(V_resistor), line=dict(color='red', dash='dash'))
)

fig.add_shape(
    dict(type='line', x0=1.5 * tau, x1=1.5 * tau, y0=0, y1=max(V_resistor), line=dict(color='red', dash='dash'))
)

# Show the interactive plot
fig.show()
