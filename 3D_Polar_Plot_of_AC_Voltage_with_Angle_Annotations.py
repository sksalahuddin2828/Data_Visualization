import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import sympy as sp
import matplotlib.pyplot as plt
from IPython.display import display, HTML
from matplotlib.animation import FuncAnimation

# Calculate the time for one complete cycle of 400-Hz AC power
frequency = 400  # in Hertz
time_period = 1 / frequency  # in seconds

# Display the result
print("Time for one complete cycle:", time_period, "seconds")

# Create a symbolic variable for the angle in radians
angle = sp.symbols('angle', real=True)

# Create a function for the AC voltage over time
voltage_function = 170 * sp.sin(angle)  # Assuming peak voltage of 170V

# Create a numpy function from the symbolic function
voltage_np = sp.lambdify(angle, voltage_function, 'numpy')

# Generate time values
angles = np.linspace(0, 2*np.pi, 1000)
voltages = voltage_np(angles)

# Create a DataFrame using pandas
data = pd.DataFrame({'Angle': angles, 'Voltage': voltages})

# Interactive 3D plot using Plotly
fig_3d = px.line_3d(data, x='Angle', y='Voltage', z=np.zeros_like(data['Angle']),
                    title='AC Voltage Behavior in 3D Space')
fig_3d.update_layout(scene=dict(xaxis_title='Angle (radians)', yaxis_title='Voltage', zaxis_title='Time'))
fig_3d.show()

# Animation of AC voltage over time using Matplotlib
fig_anim, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-180, 180)
ax.set_xlabel('Angle (radians)')
ax.set_ylabel('Voltage')
ax.set_title('AC Voltage Animation')

def animate(i):
    line.set_data(data['Angle'][:i], data['Voltage'][:i])
    return line,

ani = FuncAnimation(fig_anim, animate, frames=len(data), interval=50, blit=True)
plt.show()

# Display additional mathematical information and expressions
display(HTML("<h2>Mathematical Expressions and Information</h2>"))
display(HTML("<p>The AC voltage equation: V(angle) = 170 * sin(angle)</p>"))
display(HTML(f"<p>Time for one complete cycle: {time_period:.6f} seconds</p>"))

# Polar plot with annotations using Plotly
fig_polar_annotated = go.Figure()

fig_polar_annotated.add_trace(go.Scatterpolar(r=data['Voltage'], theta=data['Angle'], mode='lines'))

for angle_val in np.arange(0, 2 * np.pi, np.pi / 6):
    fig_polar_annotated.add_annotation(
        go.layout.Annotation(
            x=angle_val,
            y=180,
            text=f'{angle_val:.1f}',
            showarrow=False,
            font=dict(size=10)
        )
    )

fig_polar_annotated.update_layout(
    title='Polar Plot of AC Voltage with Angle Annotations',
    polar=dict(radialaxis=dict(showticklabels=False, ticksuffix='%'))
)
fig_polar_annotated.show()
