import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Step 1: Generating Data
x_values = np.linspace(-5, 5, 100)  # Generate 100 x values from -5 to 5
term1 = 1 + x_values
term2 = 1 + x_values ** 2
term3 = 1 + x_values ** 3

# Step 2: Mathematical Dance and Expressing Equations
term1_description = """
Step into the enchanting world of the Mathematical Dance of (1+x)!

The first term (1+x) gracefully performs its waltz, rising in unity with each step of x.

Mathematical Expression:
The linear term (1+x) is a linear function, y = 1 + x, where:
- The slope of the line is 1, symbolizing constant growth for each unit of x.
- The y-intercept is 1, indicating the starting point of the dance.

Theory and Real-world Application:
Linear functions are the foundation of algebra and calculus, finding use in countless real-world scenarios, such as linear motion, simple growth rates, and straight-line relationships.
"""

term2_description = """
Welcome to the mesmerizing ballet of the Mathematical Dance of (1+x²)!

The second term (1+x²) forms a symmetrical parabolic dance, showcasing its elegance.

Mathematical Expression:
The quadratic term (1+x²) is a parabolic function, y = 1 + x², where:
- The coefficient of x² is 1, leading to a smooth and symmetric parabola.
- The constant term 1 ensures the parabola never touches the origin, creating a majestic peak.

Theory and Real-world Application:
Quadratic functions are pervasive in physics, engineering, and optimization problems. They model projectile motion, predict maximum and minimum values, and describe the shape of satellite dishes.
"""

term3_description = """
Prepare to be enthralled by the soul-stirring rhapsody of the Mathematical Dance of (1+x³)!

The third term (1+x³) embodies versatility, with its multiple peaks and valleys.

Mathematical Expression:
The cubic term (1+x³) is a cubic function, y = 1 + x³, where:
- The coefficient of x³ is 1, contributing to the formation of multiple peaks and valleys.
- The constant term 1 maintains the cubic's connection to the origin.

Theory and Real-world Application:
Cubic functions have versatile applications, from designing smooth curves in computer graphics to predicting economic trends and solving cubic equations.
"""

# Step 3: Visualization using 3D Plot
fig = plt.figure(figsize=(15, 5))

# Plot for Term 1
ax1 = fig.add_subplot(131, projection='3d')
ax1.plot(x_values, term1, np.zeros_like(x_values), color='blue', alpha=0.8, linewidth=2)
ax1.set_xlabel('x')
ax1.set_ylabel('(1+x)')
ax1.set_zlabel('Contribution')
ax1.set_title('Mathematical Dance of (1+x)', fontsize=12)

# Plot for Term 2
ax2 = fig.add_subplot(132, projection='3d')
ax2.plot(x_values, term2, np.zeros_like(x_values), color='red', alpha=0.8, linewidth=2)
ax2.set_xlabel('x')
ax2.set_ylabel('(1+x²)')
ax2.set_zlabel('Contribution')
ax2.set_title('Mathematical Dance of (1+x²)', fontsize=12)

# Plot for Term 3
ax3 = fig.add_subplot(133, projection='3d')
ax3.plot(x_values, term3, np.zeros_like(x_values), color='green', alpha=0.8, linewidth=2)
ax3.set_xlabel('x')
ax3.set_ylabel('(1+x³)')
ax3.set_zlabel('Contribution')
ax3.set_title('Mathematical Dance of (1+x³)', fontsize=12)

plt.tight_layout()
plt.show()

# Step 4: Presentation and Explanation
print(term1_description)
print(term2_description)
print(term3_description)
