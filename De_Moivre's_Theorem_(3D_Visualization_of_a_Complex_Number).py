import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def de_moivre_theorem(n, theta):
    # De Moivre's Theorem: (cos θ + i sin θ)^n = cos (nθ) + i sin (nθ)
    return np.cos(n * theta) + 1j * np.sin(n * theta)

def plot_complex_number_in_3d(z):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Extract the real, imaginary, and modulus parts of the complex number
    real_part = z.real
    imag_part = z.imag
    modulus = np.abs(z)

    # Plot the complex number in 3D
    ax.quiver(0, 0, 0, real_part, imag_part, modulus, color='b', label='Complex Number')

    # Plot the real part (x-axis)
    ax.quiver(0, 0, 0, real_part, 0, 0, color='r', label='Real Part')

    # Plot the imaginary part (y-axis)
    ax.quiver(real_part, 0, 0, 0, imag_part, 0, color='g', label='Imaginary Part')

    ax.set_xlim([-1.5, 1.5])
    ax.set_ylim([-1.5, 1.5])
    ax.set_zlim([0, 2.0])
    ax.set_xlabel('Re')
    ax.set_ylabel('Im')
    ax.set_zlabel('|z|')
    ax.set_title(f"3D Visualization of a Complex Number (n={n}, θ={theta} radians)")
    ax.legend()

    plt.show()

if __name__ == "__main__":
    # Example: De Moivre's Theorem
    n = 3
    theta = np.pi / 4  # 45 degrees in radians

    complex_power = de_moivre_theorem(n, theta)
    print(f"De Moivre's Theorem: (cos({theta}) + i*sin({theta}))^{n} = {complex_power}")

    # 3D Visualization of the complex number
    plot_complex_number_in_3d(complex_power)
