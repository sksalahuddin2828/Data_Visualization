import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from IPython.display import display, clear_output
import time

# Given values
V = 12.0  # Voltage (in volts)
R1 = 1.00  # Resistance of R1 (in ohms)
R2 = 6.00  # Resistance of R2 (in ohms)
R3 = 13.00  # Resistance of R3 (in ohms)

# Create a function to calculate current at a specific time t
def calculate_current(t):
    R_eq = 1 / (1 / R2 + 1 / R3)
    R_total = R1 + R_eq
    I_total = V / R_total
    I2 = I_total * (R3 / (R2 + R3))
    I3 = V / R3

    if t < 0:
        return 0
    elif t < 1:
        return I_total * t
    elif t < 2:
        return I_total
    elif t < 3:
        return I2
    else:
        return I3

# Create a time vector for animation
t_values = np.linspace(-1, 4, 500)

# Create a pandas DataFrame to store calculated values at each time step
data = {
    "Time (s)": t_values,
    "Current (A)": [calculate_current(t) for t in t_values],
}
df = pd.DataFrame(data)

# Create an interactive line plot of current vs. time
fig = px.line(df, x="Time (s)", y="Current (A)", title="Current vs. Time")
fig.update_xaxes(title_text="Time (s)")
fig.update_yaxes(title_text="Current (A)")
fig.update_layout(annotations=[
    {
        "text": "0-1s: Current ramps up",
        "x": 0.5,
        "y": 2,
        "showarrow": False,
        "font": {"size": 12},
    },
    {
        "text": "1-2s: Steady state",
        "x": 1.5,
        "y": 4,
        "showarrow": False,
        "font": {"size": 12},
    },
    {
        "text": "2-3s: Current through R2",
        "x": 2.5,
        "y": 1.5,
        "showarrow": False,
        "font": {"size": 12},
    },
    {
        "text": "3-4s: Current through R3",
        "x": 3.5,
        "y": 0.5,
        "showarrow": False,
        "font": {"size": 12},
    },
])

# Define a custom animation function
def animate_current(frame):
    fig.update_traces(y=[calculate_current(frame)], selector=dict(type='scatter'))

# Create an animation for the current vs. time plot
animation_frames = len(t_values)
for frame in range(animation_frames):
    animate_current(frame)
    display(fig)
    clear_output(wait=True)
    time.sleep(0.01)

# Add mathematical expressions and theory alongside the animation
markdown_text = """
**Circuit Explanation**

- The circuit consists of a battery with a voltage of {} V.
- Resistor R1 has a resistance of {} ohms.
- Resistor R2 has a resistance of {} ohms, and R3 has a resistance of {} ohms.
- Initially (0-1s), the current ramps up as the capacitors charge.
- In the steady state (1-2s), the total current is constant.
- During 2-3s, the current flows mainly through R2.
- In the final phase (3-4s), the current flows primarily through R3.

**Mathematical Expressions**

- Equivalent resistance for R2 and R3 in parallel: $R_{{eq}} = \\frac{{R2 \\cdot R3}}{{R2 + R3}}$
- Total resistance of the circuit: $R_{{total}} = R1 + R_{{eq}}$
- Total current (Ohm's Law): $I = \\frac{{V}}{{R_{{total}}}}$
- Current through R2 (Current Divider Rule): $I2 = I \\cdot \\frac{{R3}}{{R2 + R3}}$
- Current through R3 (Ohm's Law): $I3 = \\frac{{V}}{{R3}}$

""".format(V, R1, R2, R3)

# Display the explanation and animation
display(fig)
print(markdown_text)
