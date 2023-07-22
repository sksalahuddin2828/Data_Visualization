import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def euler_theorem(x):
    # Euler's Theorem: e^(ix) = cos(x) + i*sin(x)
    return np.cos(x) + 1j * np.sin(x)

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
    ax.set_title('3D Visualization of a Complex Number')
    ax.legend()

    plt.show()

if __name__ == "__main__":
    # Example 1: Euler's Theorem
    angle_radians = np.pi / 4  # 45 degrees in radians
    complex_exponential = euler_theorem(angle_radians)
    print(f"Euler's Theorem: e^(i{angle_radians}) = {complex_exponential}")

    # Example 2: Complex Number in Polar Form
    r = 2.0
    theta = np.pi / 3  # 60 degrees in radians
    z = r * euler_theorem(theta)
    print(f"Complex Number in Polar Form: z = {r} * (cos({theta}) + i*sin({theta})) = {z}")

    # Example 3: Plotting the Complex Number in 3D
    plot_complex_number_in_3d(z)
