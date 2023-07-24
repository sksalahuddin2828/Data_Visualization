import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Create figure and axis
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Function to update the plot animation based on the degree
def update(degree):
    ax.clear()

    # Generate random coefficients for the polynomial
    coefficients = np.random.randn(degree + 1)

    # Solve the polynomial roots
    roots = np.roots(coefficients)

    # Plot the roots as dancing particles in 3D space
    real_parts = roots.real
    imag_parts = roots.imag
    ax.scatter(real_parts, imag_parts, np.zeros_like(roots), c=np.angle(roots), cmap='hsv', s=150 + degree*25, marker='o')

    # Set plot properties
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_zlim(-1, 1)
    ax.set_xlabel('Real')
    ax.set_ylabel('Imaginary')
    ax.set_zlabel('Degree')
    ax.set_title(f'Mathematical Dance of Polynomials (Degree: {degree})')

    # Show the polynomial equation
    equation_str = generate_equation_str(coefficients)
    ax.text(-5, -5, 1, equation_str, fontsize=12, color='black', ha='left', va='top')

    # Show Galois Group information
    galois_group_str = get_galois_group(degree)
    ax.text(-5, -5, 0.8, f"Galois Group: {galois_group_str}", fontsize=10, color='black', ha='left', va='top')

    # Add legend
    legend = ax.legend(loc='upper right', title='Degree', labels=[f'Degree {d}' for d in range(2, 11)], frameon=False)
    legend.get_title().set_fontsize(12)

# Function to generate the polynomial equation string
def generate_equation_str(coefficients):
    equation_str = 'Equation: '
    for i, coef in enumerate(coefficients[::-1]):
        if coef != 0:
            if i > 0:
                equation_str += f" + " if coef > 0 else f" - "
            if abs(coef) != 1 or i == len(coefficients) - 1:
                equation_str += f"{abs(coef):.2f}"
            if i < len(coefficients) - 1:
                equation_str += f"x^{len(coefficients) - 1 - i}"
    return equation_str

# Function to get the Galois Group information
def get_galois_group(degree):
    if degree <= 4:
        return "Solvable"
    else:
        return "Not Solvable (Unsolvable by Radicals)"

# Function to create the animation
def animate_polynomials():
    degrees = np.arange(2, 11)  # Degrees from 2 to 10

    anim = FuncAnimation(fig, update, frames=degrees, interval=3000, repeat=True)

    # Save the animation as an mp4 video (optional)
    anim.save('mathematical_dance_of_polynomials.mp4', dpi=150)

    plt.show()

# Start the animation
animate_polynomials()
