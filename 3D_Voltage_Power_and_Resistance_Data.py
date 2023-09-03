import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import sympy as sp
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define resistances
resistors = {'R1': 2, 'R2': 3, 'R3': 4}

# Calculate total resistance
total_resistance = sum(resistors.values())

# Generate current values
current_values = np.linspace(0.1, 5, 100)

# Calculate voltage and power for each resistor
data = {'Current (I)': current_values}
for resistor, resistance in resistors.items():
    data[f'Voltage ({resistor})'] = current_values * resistance
    data[f'Power ({resistor})'] = (current_values ** 2) * resistance

# Create a DataFrame
df = pd.DataFrame(data)

# Create interactive 3D plot using Plotly
fig = make_subplots(rows=2, cols=2, subplot_titles=('Voltage vs. Current', 'Power vs. Current', 'Resistance vs. Current', 'Current Animation'))

for i, resistor in enumerate(resistors.keys()):
    row = i // 2 + 1
    col = i % 2 + 1
    fig.add_trace(go.Scatter(x=df['Current (I)'], y=df[f'Voltage ({resistor})'], mode='lines', name=f'Voltage ({resistor})'), row=row, col=col)
    fig.add_trace(go.Scatter(x=df['Current (I)'], y=df[f'Power ({resistor})'], mode='lines', name=f'Power ({resistor})'), row=row, col=col)
    fig.add_trace(go.Scatter(x=df['Current (I)'], y=np.full_like(df['Current (I)'], resistors[resistor]), mode='lines', name=f'Resistance ({resistor})'), row=row, col=col)

# Create an interactive table using Plotly
table = go.Figure(data=[go.Table(
    header=dict(values=list(df.columns)),
    cells=dict(values=[df[col] for col in df.columns]))
])
table.update_layout(title='Voltage, Power, and Resistance Data')

# Define a symbolic variable for animation
t = sp.symbols('t')

# Create an animation function to visualize current changing over time
def animate_current(t):
    current = 5 * np.sin(2 * np.pi * t) + 5
    return current

# Create a matplotlib animation of current changing over time
fig_animation, ax = plt.subplots()
current_animation_line, = ax.plot([], [], lw=2)
ax.set_xlim(0, 1)
ax.set_ylim(0, 10)
ax.set_xlabel('Time')
ax.set_ylabel('Current (I)')

def update(frame):
    t = frame / 100
    current = animate_current(t)
    current_animation_line.set_data([t, t], [0, current])
    return current_animation_line,

animation = FuncAnimation(fig_animation, update, frames=100, interval=50)

# Display the figures using Plotly
fig.show()
table.show()

# Display the current animation
plt.show()
