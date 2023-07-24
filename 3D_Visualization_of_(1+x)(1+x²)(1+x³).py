import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Step 1: Generating Data
x_values = np.linspace(-5, 5, 100)  # Generate 100 x values from -5 to 5
expression_values = (1 + x_values) * (1 + x_values ** 2) * (1 + x_values ** 3)

# Step 2: Mathematical Dance and Expressing Equations
expression_description = """
The expression (1+x)(1+x²)(1+x³) can be broken down as follows:

1. The first term (1+x) represents the linear contribution.
2. The second term (1+x²) represents the quadratic contribution, peaking at x=0.
3. The third term (1+x³) represents the cubic contribution, having both positive and negative peaks.

As we vary x, we witness the dance of these terms, interacting to create the final expression.
"""

# Step 3: Visualization using 3D Plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

X, Y = np.meshgrid(x_values, expression_values)
Z = np.zeros_like(X)

ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)

ax.set_xlabel('x')
ax.set_ylabel('(1+x)(1+x²)(1+x³)')
ax.set_zlabel('Z')
ax.set_title('3D Visualization of (1+x)(1+x²)(1+x³)', fontsize=16)

plt.show()

# Step 4: Presentation and Explanation
print(expression_description)
