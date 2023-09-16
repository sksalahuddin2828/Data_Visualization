import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Define the symbolic variable theta
theta = sp.symbols('theta')

# Calculate secant in terms of sine
sec_sine = 1 / sp.sqrt(1 - sp.sin(theta)**2)

# Calculate secant in terms of tangent
sec_tangent = sp.sqrt(1 + sp.tan(theta)**2)

# Create a numpy function for secant in terms of sine
sec_sine_func = sp.lambdify(theta, sec_sine, 'numpy')

# Create a numpy function for secant in terms of tangent
sec_tangent_func = sp.lambdify(theta, sec_tangent, 'numpy')

# Generate data for theta values
theta_values = np.linspace(0, 2 * np.pi, 1000)

# Calculate secant values
sec_sine_values = sec_sine_func(theta_values)
sec_tangent_values = sec_tangent_func(theta_values)

# Create plots
plt.figure(figsize=(10, 5))
plt.subplot(121)
plt.plot(theta_values, sec_sine_values, label='sec(theta) = 1/sqrt(1-sin^2(theta))')
plt.xlabel('Theta')
plt.ylabel('sec(theta)')
plt.title('Secant in Terms of Sine')
plt.legend()

plt.subplot(122)
plt.plot(theta_values, sec_tangent_values, label='sec(theta) = sqrt(1+tan^2(theta))')
plt.xlabel('Theta')
plt.ylabel('sec(theta)')
plt.title('Secant in Terms of Tangent')
plt.legend()

plt.tight_layout()
plt.show()
