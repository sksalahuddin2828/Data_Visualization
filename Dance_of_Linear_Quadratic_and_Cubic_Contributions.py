import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Step 1: Generating Data
x_values = np.linspace(-5, 5, 100)  # Generate 100 x values from -5 to 5
linear_contribution = 1 + x_values
quadratic_contribution = 1 + x_values ** 2
cubic_contribution = 1 + x_values ** 3
expression_values = linear_contribution * quadratic_contribution * cubic_contribution

# Step 2: Mathematical Dance and Expressing Equations
expression_description = """
Let's explore the mesmerizing dance of the contributions within the expression (1+x)(1+x²)(1+x³)!

1. Linear Contribution: The first term (1+x) represents the linear contribution.
   Visualize it as a graceful linear ascent, growing steadily as x increases.

2. Quadratic Contribution: The second term (1+x²) represents the quadratic contribution, peaking at x=0.
   Picture this as a splendid parabolic curve, symmetrically rising and falling.

3. Cubic Contribution: The third term (1+x³) represents the cubic contribution, having both positive and negative peaks.
   Imagine it as a magnificent cubic journey, with multiple crests and troughs.

Now, let's combine these beautiful dances to form the grand finale - the expression (1+x)(1+x²)(1+x³)!
"""

# Step 3: Visualization using 3D Plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

X, Y_linear = np.meshgrid(x_values, linear_contribution)
Y_quadratic = np.meshgrid(x_values, quadratic_contribution)[1]
Y_cubic = np.meshgrid(x_values, cubic_contribution)[1]

ax.plot_surface(X, Y_linear, Y_quadratic, cmap='Blues', alpha=0.7)
ax.plot_surface(X, Y_linear, Y_cubic, cmap='Reds', alpha=0.7)

ax.set_xlabel('x')
ax.set_ylabel('(1+x)')
ax.set_zlabel('Contribution')
ax.set_title('Dance of Linear, Quadratic, and Cubic Contributions', fontsize=16)

# Adding a legend for the contributions
ax.legend(
    [plt.Rectangle((0, 0), 1, 1, fc='b', alpha=0.7), plt.Rectangle((0, 0), 1, 1, fc='r', alpha=0.7)],
    ['Quadratic Contribution', 'Cubic Contribution'],
    loc='upper right',
)

plt.show()

# Step 4: Presentation and Explanation
print(expression_description)
