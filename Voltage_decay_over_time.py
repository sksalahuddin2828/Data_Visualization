import numpy as np
import pandas as pd
import plotly.express as px
import sympy as sp

# Constants
V0 = 10000  # Initial voltage in volts
decay_factor = 0.368
time_intervals = np.array([0, 8.0, 16.0, 24.0])  # Time intervals in milliseconds

# Calculate voltage at each time interval
voltages = V0 * (decay_factor ** (time_intervals / 8.0))

# Create a pandas DataFrame to store the data
data = pd.DataFrame({'Time (ms)': time_intervals, 'Voltage (V)': voltages})

# Create an interactive plot with Plotly
fig = px.line(data, x='Time (ms)', y='Voltage (V)', title='Voltage Decay Over Time')
fig.update_xaxes(title_text='Time (ms)')
fig.update_yaxes(title_text='Voltage (V)')
fig.show()

# Symbolic calculation using sympy
t_symbolic = sp.symbols('t')
voltage_symbolic = V0 * (decay_factor ** (t_symbolic / 8.0))
solution = sp.solve(voltage_symbolic - V0 * 0.5, t_symbolic)
print(f'Time for voltage to reach 50% of initial value: {solution[0]} ms')
