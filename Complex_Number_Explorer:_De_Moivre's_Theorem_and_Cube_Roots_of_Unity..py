import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def de_moivre_theorem(z, n):
    # Validate De Moivre's Theorem: z^n + 1/z^n = 2*cos(nθ) and z^n - 1/z^n = 2i*sin(nθ)
    zn = z ** n
    zn_inv = 1 / zn
    left_sum = zn + zn_inv
    left_diff = zn - zn_inv
    right_sum = 2 * np.cos(n * np.angle(z))
    right_diff = 2j * np.sin(n * np.angle(z))

    return left_sum, right_sum, left_diff, right_diff

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
    ax.set_title(f"3D Visualization of a Complex Number (z = {z})")
    ax.legend()

    plt.show()

if __name__ == "__main__":
    # Example: Validate De Moivre's Theorem
    z = np.exp(1j * np.pi / 4)  # z = cos(π/4) + i*sin(π/4)
    n = 3

    left_sum, right_sum, left_diff, right_diff = de_moivre_theorem(z, n)
    print(f"Validation of De Moivre's Theorem (n={n}, z={z}):")
    print(f"z^n + 1/z^n = {left_sum} | 2*cos(nθ) = {right_sum}")
    print(f"z^n - 1/z^n = {left_diff} | 2i*sin(nθ) = {right_diff}")

    # 3D Visualization of the complex number
    plot_complex_number_in_3d(z)
