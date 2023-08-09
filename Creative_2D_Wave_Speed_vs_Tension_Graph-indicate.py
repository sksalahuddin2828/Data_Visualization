import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Step 1: Deriving the Wave Speed Equation
v, FT, mu = sp.symbols('v FT mu')
wave_speed_equation = sp.sqrt(FT / mu)

# Print the derived equation
print("Derived Wave Speed Equation:", wave_speed_equation)

# Step 2: Calculating Wave Speed
tension_value = 100.0  # Example value for tension (replace with your value)
linear_density_value = 0.01  # Example value for linear density (replace with your value)
calculated_wave_speed = wave_speed_equation.subs([(FT, tension_value), (mu, linear_density_value)])
print("Calculated Wave Speed:", calculated_wave_speed)

# Step 3: Visualization
tension_range = np.linspace(1, 200, 100)
wave_speed_values = [wave_speed_equation.subs([(FT, T), (mu, linear_density_value)]) for T in tension_range]

# Create a plot with LaTeX rendering
plt.figure()
plt.plot(tension_range, wave_speed_values)
plt.xlabel('Tension ($F_T$)')
plt.ylabel('Wave Speed ($v$)')
plt.title('Wave Speed vs Tension')
plt.grid()

# Add annotations
plt.annotate('Maximum Wave Speed', xy=(150, np.max(wave_speed_values)),
             xytext=(120, np.max(wave_speed_values) + 200),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=12)

plt.show()
