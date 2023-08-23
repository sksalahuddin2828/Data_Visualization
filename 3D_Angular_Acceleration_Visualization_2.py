import numpy as np
import pandas as pd
import sympy as sp
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Given data
t_values = np.linspace(0, 10, 100)  # Time values
alpha_values = 20.0 * (2 * np.pi) - 0.1 * t_values  # Angular acceleration values

# Create a DataFrame
data = {'Time (s)': t_values, 'Angular Acceleration (rad/s^2)': alpha_values}
df = pd.DataFrame(data)

# Calculate angular velocity and displacement using symbolic calculations
t = sp.Symbol('t')
alpha = 20.0 * (2 * np.pi) - 0.1 * t
angular_velocity = sp.integrate(alpha, (t, 0, t))
displacement = sp.integrate(angular_velocity, (t, 0, t))

# Convert symbolic expressions to numeric values
angular_velocity_numeric = angular_velocity.subs('t', 10).evalf()
displacement_numeric = displacement.subs('t', 10).evalf()

# Display numeric results
print("Angular Velocity:", angular_velocity_numeric)
print("Displacement:", displacement_numeric)

# Interactive Plot using Plotly with Theory Explanation
fig = go.Figure()

fig.add_trace(go.Scatter(x=df['Time (s)'], y=df['Angular Acceleration (rad/s^2)'],
                    mode='lines',
                    name='Angular Acceleration'))

fig.update_layout(title='Angular Acceleration over Time',
                  xaxis_title='Time (s)',
                  yaxis_title='Angular Acceleration (rad/s^2)')

fig.add_annotation(
    text="Deceleration with Time",
    x=6, y=10,
    arrowhead=2,
    arrowsize=1,
    arrowwidth=2,
    arrowcolor="red"
)

fig.show()

# 3D Angular Acceleration Plot using Matplotlib
fig_3d = plt.figure()
ax = fig_3d.add_subplot(111, projection='3d')
ax.plot(t_values, alpha_values, zs=0, zdir='y', label='Angular Acceleration')
ax.set_xlabel('Time (s)')
ax.set_ylabel('Angular Acceleration (rad/s^2)')
ax.set_zlabel('Value')
ax.legend()
plt.title('3D Angular Acceleration Visualization')
plt.show()

# Animation using Matplotlib's FuncAnimation
fig_anim, ax_anim = plt.subplots()
ax_anim.set_xlim(0, 10)
ax_anim.set_ylim(0, 60)
line, = ax_anim.plot([], [], lw=2)

def animate(i):
    x = t_values[:i+1]
    y = alpha_values[:i+1]
    line.set_data(x, y)
    return line,

ani = FuncAnimation(fig_anim, animate, frames=len(t_values), interval=100, blit=True)
plt.title('Angular Acceleration Animation')
plt.xlabel('Time (s)')
plt.ylabel('Angular Acceleration (rad/s^2)')
plt.show()
