import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from IPython.display import display, HTML
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

# Given data
voltage = 240e3  # Volts
resistance_per_insulator = 1.00e9  # Ohms
power_transmitted = 5.00e2  # Watts

# Function to calculate power dissipated
def calculate_power_dissipated(num_insulators):
    total_resistance = 1 / (1 / resistance_per_insulator * num_insulators)
    current = voltage / total_resistance
    power_dissipated = current ** 2 * total_resistance
    return power_dissipated

# Create a DataFrame for visualization
num_insulators_range = np.arange(1, 101)
power_dissipated_range = [calculate_power_dissipated(n) for n in num_insulators_range]
df = pd.DataFrame({"Number of Insulators": num_insulators_range, "Power Dissipated (Watts)": power_dissipated_range})

# Visualize the resistance of insulators
fig1 = px.line(df, x="Number of Insulators", y="Power Dissipated (Watts)",
                title="Power Dissipated by Insulators",
                labels={"Number of Insulators": "Number of Insulators", "Power Dissipated (Watts)": "Power Dissipated (Watts)"})
fig1.update_xaxes(nticks=20)

# Create an animation of power dissipation
fig2, ax = plt.subplots()
x_data = []
y_data = []
ln, = plt.plot([], [], 'ro', markersize=8, label='Power Dissipated')
ax.set_xlim(0, 110)
ax.set_ylim(0, max(power_dissipated_range) + 10)
ax.set_xlabel("Number of Insulators")
ax.set_ylabel("Power Dissipated (Watts)")
ax.set_title("Animation: Power Dissipation with Insulators")

def init():
    ln.set_data([], [])
    return ln,

def update(frame):
    x_data.append(num_insulators_range[frame])
    y_data.append(power_dissipated_range[frame])
    ln.set_data(x_data, y_data)
    return ln,

ani = FuncAnimation(fig2, update, frames=len(num_insulators_range), init_func=init, blit=True)

# Display animated plot
plt.legend()
plt.close(fig2)  # Prevents initial rendering from showing
HTML(ani.to_jshtml())

# Print explanation and expressions
explanation = """
<strong>Explanation:</strong><br>
As the number of ceramic insulators increases, the total resistance to ground decreases. This leads to an increase in the current passing through the insulators. Using Ohm's law (V = IR), we can calculate the current for each configuration of insulators. The power dissipated is given by P = I^2 * R.
<br><br>
<strong>Mathematical Expression:</strong><br>
Total Resistance (R_total) = 1 / (1 / R_insulator * N)
Current (I) = Voltage / R_total
Power Dissipated (P) = I^2 * R_total
<br><br>
<strong>Theory:</strong><br>
In this scenario, insulators are connected in parallel, resulting in a reciprocal relationship between their resistances and the total resistance. The power dissipated is directly proportional to the square of the current and the total resistance. As the number of insulators increases, the total resistance decreases, allowing more current to flow, leading to higher power dissipation.
"""

display(HTML(explanation))

# Display visualizations
fig1.show()
