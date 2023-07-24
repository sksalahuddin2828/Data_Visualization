import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def f1(n):
    return 4 * n + 3

def f2(n):
    return 20 * n**2 + 5 * n + 2

def g1(n):
    return n

def g2(n):
    return n**2

def visualize_time_complexity(fn, gn, fn_name, gn_name, notation):
    n = np.linspace(1, 10, 100)
    f_values = fn(n)
    g_values = gn(n)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(n, f_values, g_values, s=50, c='b', marker='o', label=fn_name)
    ax.scatter(n, g_values, f_values, s=50, c='r', marker='x', label=gn_name)

    ax.set_xlabel('n')
    ax.set_ylabel('f(n)')
    ax.set_zlabel('g(n)')

    plt.title(f'{notation} Notation - {fn_name} vs {gn_name} Functions')
    plt.legend()
    plt.show()

# Visualize O notation for Example 1
visualize_time_complexity(f1, g1, 'f(n) = 4n + 3', 'g(n) = n', 'O')

# Visualize O notation for Example 2
visualize_time_complexity(f2, g2, 'f(n) = 20n^2 + 5n + 2', 'g(n) = n^2', 'O')

# Visualize Ω notation for Example 1
visualize_time_complexity(f1, g1, 'f(n) = 4n + 3', 'g(n) = n', 'Ω')

# Visualize Ω notation for Example 2
visualize_time_complexity(f2, g2, 'f(n) = 20n^2 + 5n + 2', 'g(n) = n^2', 'Ω')

# Visualize θ notation for Example 1
visualize_time_complexity(f1, g1, 'f(n) = 4n + 3', 'g(n) = n', 'θ')

# Visualize θ notation for Example 2
visualize_time_complexity(f2, g2, 'f(n) = 20n^2 + 5n + 2', 'g(n) = n^2', 'θ')
