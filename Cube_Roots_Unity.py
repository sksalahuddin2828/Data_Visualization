import numpy as np
import matplotlib.pyplot as plt

def calculate_cube_roots_of_unity():
    # Calculate the cube roots of unity
    theta_values = [0, 2 * np.pi / 3, 4 * np.pi / 3]
    roots = np.cos(theta_values) + 1j * np.sin(theta_values)
    return roots

def validate_de_moivre_theorem(z, n):
    # Validate De Moivre's Theorem: z^n + 1/z^n = 2*cos(nθ) and z^n - 1/z^n = 2i*sin(nθ)
    zn = z ** n
    zn_inv = 1 / zn
    left_side_sum = zn + zn_inv
    left_side_diff = zn - zn_inv
    right_side_sum = 2 * np.cos(n * np.angle(z))
    right_side_diff = 2j * np.sin(n * np.angle(z))

    return left_side_sum, right_side_sum, left_side_diff, right_side_diff

def plot_complex_numbers_on_plane(numbers, title="Complex Numbers on the Complex Plane"):
    fig, ax = plt.subplots()

    # Plot complex numbers on the complex plane
    ax.scatter(numbers.real, numbers.imag, color='b', label='Cube Roots of Unity')

    ax.axhline(y=0, color='k', linewidth=0.5)
    ax.axvline(x=0, color='k', linewidth=0.5)

    ax.set_xlabel('Real')
    ax.set_ylabel('Imaginary')
    ax.set_title(title)
    ax.grid(True)
    ax.legend()

    plt.show()

if __name__ == "__main__":
    # Example: Cube Roots of Unity
    cube_roots = calculate_cube_roots_of_unity()
    print("Cube Roots of Unity:")
    for idx, root in enumerate(cube_roots):
        print(f"Root {idx+1}: {root}")

    # 2D Visualization of Cube Roots of Unity
    plot_complex_numbers_on_plane(cube_roots, title="Cube Roots of Unity")

    # Example: Validate De Moivre's Theorem
    z = np.exp(1j * np.pi / 4)  # z = cos(π/4) + i*sin(π/4)
    n = 3
    left_sum, right_sum, left_diff, right_diff = validate_de_moivre_theorem(z, n)
    print(f"Validation of De Moivre's Theorem (n={n}):")
    print(f"z^n + 1/z^n = {left_sum} | 2*cos(nθ) = {right_sum}")
    print(f"z^n - 1/z^n = {left_diff} | 2i*sin(nθ) = {right_diff}")



# Answer: Cube Roots of Unity:
#         Root 1: (1+0j)
#         Root 2: (-0.4999999999999998+0.8660254037844387j)
#         Root 3: (-0.5000000000000004-0.8660254037844384j)

#         Validation of De Moivre's Theorem (n=3):
#         z^n + 1/z^n = (-1.4142135623730947+0j) | 2*cos(nθ) = -1.414213562373095
#         z^n - 1/z^n = 1.4142135623730954j | 2i*sin(nθ) = 1.4142135623730951j
