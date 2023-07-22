import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_complex_numbers(z_values, title):
    real_part = np.real(z_values)
    imag_part = np.imag(z_values)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(real_part, imag_part, 0, c='b', marker='o')
    ax.set_xlabel('Re')
    ax.set_ylabel('Im')
    ax.set_zlabel('0')
    ax.set_title(title)
    plt.show()

# Example usage
omega = np.roots([1, 0, 0, 1])  # Calculate cube roots of unity
plot_complex_numbers(omega, 'Cube Roots of Unity')
