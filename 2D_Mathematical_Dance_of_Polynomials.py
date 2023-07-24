import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Create figure and axis
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Function to update the plot animation based on the degree
def update(degree):
    ax.clear()

    # Generate random coefficients for the polynomial
    coefficients = np.random.randn(degree + 1)

    # Solve the polynomial roots
    roots = np.roots(coefficients)

    # Plot the roots as dancing particles in 3D space
    ax.scatter(roots.real, roots.imag, np.zeros_like(roots), c='blue', s=100 + degree*20, marker='o')

    # Set plot properties
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_zlim(-1, 1)
    ax.set_xlabel('Real')
    ax.set_ylabel('Imaginary')
    ax.set_zlabel('Degree')
    ax.set_title(f'Mathematical Dance of Polynomials (Degree: {degree})')

# Function to create the animation
def animate_polynomials():
    degrees = np.arange(2, 11)  # Degrees from 2 to 10

    anim = FuncAnimation(fig, update, frames=degrees, interval=1000, repeat=True)
    anim.save('mathematical_dance_of_polynomials.mp4', dpi=150)
    plt.show()

# Start the animation
animate_polynomials()
