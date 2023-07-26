import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def permutation_cycle(n, k):
    # Create a permutation π of size n with a k-cycle
    pi = np.arange(1, n + 1)
    pi[k:] = np.roll(pi[k:], -k)  # Shift the elements after k to create the k-cycle
    return pi

def transposition(pi, a, b):
    # Perform the transposition that switches the contents of a and b in permutation pi
    x, y = n + 1, n + 2
    x, y = pi[-1] + 1, pi[-1] + 2
    return pi

def fix_permutation(pi):
    n = len(pi)
    fixed_pi = np.copy(pi)

    # Find unique values for x and y that are not in the original permutation
    x, y = max(pi) + 1, max(pi) + 2

    for i in range(n):
        pi_star = np.concatenate((fixed_pi, [x, y]))
        sigma = []

        for j in range(1, i + 1):
            sigma.append((x, j))
        for j in range(i + 1, n):
            sigma.append((y, j))

        for trans in sigma:
            fixed_pi = transposition(fixed_pi, *trans)

    return fixed_pi

def plot_permutation(pi, title):
    n = len(pi)
    plt.bar(np.arange(1, n + 1), pi)
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title(title)
    plt.show()

if __name__ == "__main__":
    n = 10  # Change n to the desired size of the permutation
    k = 5   # Change k to the desired size of the k-cycle

    # Generate the initial permutation
    pi_initial = permutation_cycle(n, k)
    plot_permutation(pi_initial, "Initial Permutation")

    # Fix the permutation
    pi_fixed = fix_permutation(pi_initial)
    plot_permutation(pi_fixed, "Fixed Permutation")

