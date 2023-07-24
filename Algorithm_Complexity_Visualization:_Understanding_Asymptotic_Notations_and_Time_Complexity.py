import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def f1(n):
    return 4 * n + 3

def f2(n):
    return 20 * n**2 + 5 * n + 2

def f3(n):
    return 5 * n

def g1(n):
    return n

def g2(n):
    return n**2

def visualize_functions(fn, gn, fn_name, gn_name):
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

    plt.title(f'{fn_name} vs {gn_name} Functions')
    plt.legend()
    plt.show()

# Visualize f(n) and g(n) for Example 1
visualize_functions(f1, g1, 'f(n) = 4n + 3', 'g(n) = n')

# Visualize f(n) and g(n) for Example 2
visualize_functions(f2, g2, 'f(n) = 20n^2 + 5n + 2', 'g(n) = n^2')

# Visualize f(n) and g(n) for Example 3
visualize_functions(f3, g1, 'f(n) = 5n', 'g(n) = n')
