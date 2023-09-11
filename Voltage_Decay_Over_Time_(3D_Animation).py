import numpy as np
import pandas as pd
import sympy as sp
import plotly.graph_objects as go

# Constants
V0 = 10000  # Initial voltage in volts
decay_factor = 0.368
time_intervals = np.linspace(0, 24, 100)  # Create more time intervals for smoother animation
# Calculate voltage at each time interval
voltages = V0 * (decay_factor ** (time_intervals / 8.0))

# Create a pandas DataFrame to store the data
data = pd.DataFrame({'Time (ms)': time_intervals, 'Voltage (V)': voltages})

# Calculate the time it takes to reach specific voltage levels
voltage_levels = [0.5 * V0, 0.25 * V0, 0.1 * V0]
times_to_reach_levels = []
for level in voltage_levels:
    t_symbolic = sp.symbols('t')
    voltage_symbolic = V0 * (decay_factor ** (t_symbolic / 8.0))
    solution = sp.solve(voltage_symbolic - level, t_symbolic)
    times_to_reach_levels.append(solution[0])

# Create an animated 3D plot with Plotly
fig = go.Figure()

# Add voltage decay curve
fig.add_trace(go.Scatter3d(x=data['Time (ms)'], y=data['Voltage (V)'], z=np.zeros(len(data)),
                           mode='lines+markers', line=dict(width=4), name='Voltage Decay'))

# Add points for specific voltage levels
for level, time in zip(voltage_levels, times_to_reach_levels):
    text = f'Time: {float(time):.2f} ms, Voltage: {float(level):.2f} V'  # Convert to float for JSON serialization
    fig.add_trace(go.Scatter3d(x=[float(time)], y=[float(level)], z=[0],
                               mode='markers+text', text=[text],
                               marker=dict(size=5), name=f'Voltage Level: {float(level):.2f} V'))

# Define animation frames
frames = [go.Frame(data=[go.Scatter3d(x=time_intervals[:k], y=voltages[:k], z=np.zeros(k),
                                      mode='lines+markers', line=dict(width=4))],
                   name=str(k)) for k in range(1, len(time_intervals))]

# Update plot layout
fig.update_layout(title='Voltage Decay Over Time (3D Animation)',
                  scene=dict(xaxis_title='Time (ms)', yaxis_title='Voltage (V)', zaxis_title='Zero'))

# Update the animation
fig.frames = frames

# Show the plot
fig.show()
