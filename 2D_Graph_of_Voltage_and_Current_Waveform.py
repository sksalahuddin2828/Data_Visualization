import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Given data
voltage_peak = 220  # Volts
frequency = 60  # Hz
resistance = resistance_a  # Ohms

# Calculate angular frequency
angular_frequency = 2 * np.pi * frequency

# Create time array
time = np.linspace(0, 1, 1000)  # One period

# Calculate voltage and current waveforms
voltage_waveform = voltage_peak * np.sin(angular_frequency * time)
current_waveform = voltage_waveform / resistance

# Create a figure and axis
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
plt.subplots_adjust(hspace=0.5)

# Initialize empty lines for animation
line_voltage, = ax1.plot([], [], lw=2, label='Voltage')
line_current, = ax2.plot([], [], lw=2, color='orange', label='Current')

# Set axis labels and titles
ax1.set_title('Voltage Waveform')
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Voltage (V)')
ax2.set_title('Current Waveform')
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Current (A)')

# Set axis limits
ax1.set_xlim(0, 1)
ax1.set_ylim(-250, 250)
ax2.set_xlim(0, 1)
ax2.set_ylim(-0.5, 0.5)

# Add legend
ax1.legend(loc='upper right')
ax2.legend(loc='upper right')

# Equations for dynamic annotation
equation_voltage = f'Voltage = {voltage_peak:.2f} sin({frequency}πt) V'
equation_current = f'Current = Voltage / Resistance = {voltage_peak:.2f} / {resistance:.2f} sin({frequency}πt) A'

# Add annotations
ax1.annotate(equation_voltage, xy=(0.05, 0.85), xycoords='axes fraction', fontsize=12, color='blue')
ax2.annotate(equation_current, xy=(0.05, 0.85), xycoords='axes fraction', fontsize=12, color='orange')

# Update function for animation
def update(frame):
    line_voltage.set_data(time[:frame], voltage_waveform[:frame])
    line_current.set_data(time[:frame], current_waveform[:frame])
    return line_voltage, line_current

# Create animation
ani = FuncAnimation(fig, update, frames=len(time), blit=True, interval=50)

# Show the animation
plt.show()
