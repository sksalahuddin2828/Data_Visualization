import numpy as np
import matplotlib.pyplot as plt

# Create data
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

# Create a colorful sine wave plot
plt.figure(figsize=(8, 6))
plt.plot(x, y, color='purple', linewidth=2)
plt.title("Colorful Sine Wave")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.grid(True, linestyle='--', alpha=0.7)
plt.fill_between(x, y, color='pink', alpha=0.3)  # Fill area under the curve with color
plt.show()

# Explanation of the plot
print("This colorful sine wave plot showcases the relationship between the angle 'x' and the sine value 'sin(x)'.")
print("The pink shaded region represents the area under the curve, which corresponds to the integral of sine over the given range.")
