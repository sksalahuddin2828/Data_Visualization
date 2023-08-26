# Sample Lissajous animation
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# Generate time values
t = np.linspace(0, 2*np.pi, 1000)

# Simulate AC voltages and currents
V = 220 * np.sin(2*np.pi*50*t)
I = 2 * np.sin(2*np.pi*50*t - np.pi/6)  # Phase difference of 30 degrees

# Animation function
def animate(i):
    ax.clear()
    ax.plot(V[:i], I[:i], color='blue')
    ax.set_title('Lissajous Animation')
    ax.set_xlabel('Voltage (V)')
    ax.set_ylabel('Current (A)')
    ax.grid()

fig, ax = plt.subplots()
ani = FuncAnimation(fig, animate, frames=len(V), interval=50)
plt.show()

# Perform Fourier Transform
freq = np.fft.fftfreq(len(V), t[1] - t[0])
V_freq = np.fft.fft(V)
I_freq = np.fft.fft(I)

# Visualize frequency-domain data
plt.figure(figsize=(10, 6))
plt.plot(freq, np.abs(V_freq), label='Voltage')
plt.plot(freq, np.abs(I_freq), label='Current')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('Frequency-Domain Analysis')
plt.legend()
plt.grid()
plt.show()

# Sample Lissajous figure for different phase differences
fig, axs = plt.subplots(2, 2, figsize=(10, 8))
phases = [0, np.pi/4, np.pi/2, 3*np.pi/4]
for i, ax in enumerate(axs.flatten()):
    ax.plot(V, I * np.cos(phases[i]), color='blue')
    ax.set_title(f'Phase Difference: {phases[i]:.2f}')
    ax.set_xlabel('Voltage (V)')
    ax.set_ylabel('Current (A)')
    ax.grid()
plt.tight_layout()
plt.show()

# Sample mathematical dance animation using LaTeX equations
from IPython.display import display, Math
import time

equations = [
    r'P_{\text{ave}} = I_{\text{rms}} V_{\text{rms}}',
    r'P_{\text{ave}} = \frac{V_{\text{rms}}^2}{R}',
    r'P_{\text{ave}} = I_{\text{rms}}^2 R'
]

for equation in equations:
    display(Math(equation))
    time.sleep(2)  # Pause for 2 seconds before next equation
