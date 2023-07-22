import numpy as np
import matplotlib.pyplot as plt

def calculate_nth_roots_of_unity(n):
    # Calculate the nth roots of unity
    k_values = np.arange(n)
    theta_values = 2 * np.pi * k_values / n
    roots = np.cos(theta_values) + 1j * np.sin(theta_values)
    return roots

def plot_complex_numbers_on_plane(numbers, title="Complex Numbers on the Complex Plane"):
    fig, ax = plt.subplots()

    # Plot complex numbers on the complex plane
    ax.scatter(numbers.real, numbers.imag, color='b', label='nth Roots of Unity')

    ax.axhline(y=0, color='k', linewidth=0.5)
    ax.axvline(x=0, color='k', linewidth=0.5)

    ax.set_xlabel('Real')
    ax.set_ylabel('Imaginary')
    ax.set_title(title)
    ax.grid(True)
    ax.legend()

    plt.show()

def sum_of_nth_roots_of_unity(n):
    # Calculate the sum of nth roots of unity
    roots = calculate_nth_roots_of_unity(n)
    return np.sum(roots)

if __name__ == "__main__":
    # Example: nth Roots of Unity
    n = 5

    nth_roots = calculate_nth_roots_of_unity(n)
    print(f"nth Roots of Unity (n={n}):")
    for idx, root in enumerate(nth_roots):
        print(f"Root {idx+1}: {root}")

    # 2D Visualization of nth Roots of Unity
    plot_complex_numbers_on_plane(nth_roots, title=f"{n}th Roots of Unity")

    # Calculate and print the sum of nth roots of unity
    sum_of_roots = sum_of_nth_roots_of_unity(n)
    print(f"Sum of {n}th Roots of Unity: {sum_of_roots}")
