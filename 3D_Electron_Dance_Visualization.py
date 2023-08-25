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

# Square wave signal for flickering effect
flicker = 0.5 * (1 + np.sign(np.sin(2 * np.pi * frequency * t_values)))

# Complex function to mimic a dance of electrons
def electron_dance(t):
    return np.sin(2 * np.pi * (frequency + 10) * t) + 0.5 * np.sin(2 * np.pi * (frequency - 5) * t)

# Create a figure with multiple subplots
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))

# Plot current with flicker effect
ax1.set_title('Sinusoidal Current with Flicker')
ax1.set_xlabel('Time')
ax1.set_ylabel('Current')
line1, = ax1.plot(t_values, I_values * flicker, color='blue')

# Electron dance visualization
ax2.set_title('Electron Dance Visualization')
ax2.set_xlabel('Time')
ax2.set_ylabel('Position')
line2, = ax2.plot([], [], color='green')

# Plot power with shading effect
ax3.set_title('Power Variation with Shading Effect')
ax3.set_xlabel('Time')
ax3.set_ylabel('Power')
ax3.fill_between(t_values, P_values, color='red', alpha=0.4)

# Animation update function for electron dance
def update_electron(frame):
    line2.set_data(t_values[:frame], electron_dance(t_values[:frame]))
    return line2,

ani_electron = FuncAnimation(fig, update_electron, frames=len(t_values), blit=True)

# LaTeX-style rendering for equations
ax2.text(0.5, -0.3, r'$Electron\ Dance:\ y = \sin(2 \pi (f+10) t) + 0.5 \sin(2 \pi (f-5) t)$',
         transform=ax2.transAxes, fontsize=12, ha='center')

# Display animations
display(HTML(ani_electron.to_jshtml()))
plt.show()
