import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Given wave function
x, t, A, k, w = sp.symbols('x t A k w')
y = A * sp.sin(k*x - w*t)

# Substituting the given values
wave_function = y.subs({A: 0.2, k: 6.28, w: 1.57})

# Finding the amplitude, wavelength, period, and speed of the wave
amplitude = wave_function.coeff(A)
wave_number = sp.solve(wave_function - A*sp.sin(k*x - w*t), k)[0]
angular_frequency = sp.solve(wave_function - A*sp.sin(k*x - w*t), w)[0]

# Create a lambda function for evaluating the numerical value of wavelength
wavelength_func = sp.lambdify((x, t, A, k, w), 2 * sp.pi / k, "numpy")
wavelength_value = wavelength_func(0, 0, 0.2, 6.28, 1.57)

period = 2 * sp.pi / angular_frequency
wave_speed = angular_frequency / wave_number

print("Amplitude:", amplitude)
print("Wave number (k):", wave_number)
print("Angular frequency (ω):", angular_frequency)
print("Wavelength:", wavelength_value)
print("Period:", period)
print("Wave speed:", wave_speed)

# Visualization of the wave function
x_values = np.linspace(0, 2 * wavelength_value, 100)
y_values = [wave_function.subs({x: val, t: 0}) for val in x_values]

plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, label='Wave Function')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title('Traveling Wave on a String')
plt.legend()
plt.grid(True)
plt.show()
