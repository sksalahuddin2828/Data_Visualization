import numpy as np
import matplotlib.pyplot as plt

# Visualization of a pulse wave
def pulse_wave(x, A, v):
    return A * np.exp(-x/v)

x_values = np.linspace(0, 10, 100)
A = 1.0  # Amplitude
v = 2.0  # Wave speed

plt.figure(figsize=(8, 6))
plt.plot(x_values, pulse_wave(x_values, A, v), label='Pulse Wave')
plt.xlabel('x (m)')
plt.ylabel('Amplitude')
plt.title('Pulse Wave with Constant Wave Speed')
plt.legend()
plt.grid(True)
plt.show()
