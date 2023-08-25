import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML, display, Markdown

# Constants
frequency = 120  # Hz
t_values = np.linspace(0, 1, 1000)  # Time values

# Calculate current using I = V/R and sinusoidal voltage
V0 = 1  # Example voltage
R = 1   # Example resistance
I_values = (V0 / R) * np.sin(2 * np.pi * frequency * t_values)

# Calculate power using P = I * V
P_values = I_values * V0

# Set up the figure and axis
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 10))

# Plot current
ax1.set_title('Sinusoidal Current')
ax1.set_xlabel('Time')
ax1.set_ylabel('Current')
line1, = ax1.plot(t_values, I_values, color='blue')

# Plot power
ax2.set_title('Power Variation')
ax2.set_xlabel('Time')
ax2.set_ylabel('Power')
line2, = ax2.plot(t_values, P_values, color='red')

# LaTeX-style rendering
ax1.text(0.5, -0.3, r'$I(t) = \frac{V_0}{R} \sin(2 \pi f t)$', transform=ax1.transAxes, fontsize=14, ha='center')
ax2.text(0.5, -0.3, r'$P(t) = I(t) \cdot V_0$', transform=ax2.transAxes, fontsize=14, ha='center')

# Animation update function
def update(frame):
    line1.set_ydata(I_values + np.sin(frame / 10))
    line2.set_ydata(P_values + np.sin(frame / 10))
    return line1, line2

ani = FuncAnimation(fig, update, frames=np.arange(0, 100), blit=True)

# Display the animation
display(HTML(ani.to_jshtml()))
