import numpy as np

set_A = np.array([1, 2, 3])
set_B = np.array([3, 4, 5])

def union(set1, set2):
    return np.union1d(set1, set2)

def intersection(set1, set2):
    return np.intersect1d(set1, set2)

import matplotlib.pyplot as plt

def plot_venn_diagram(set1, set2):
    plt.figure()
    plt.title("Venn Diagram")
    plt.gca().set_axis_on()
    plt.gca().add_patch(plt.Circle((0.3, 0.5), 0.25, color='blue', alpha=0.5))
    plt.gca().add_patch(plt.Circle((0.7, 0.5), 0.25, color='green', alpha=0.5))
    plt.gca().text(0.3, 0.5, "A", va='center', ha='center', fontsize=12)
    plt.gca().text(0.7, 0.5, "B", va='center', ha='center', fontsize=12)
    plt.gca().text(0.5, 0.5, "A ∩ B", va='center', ha='center', fontsize=12)
    plt.gca().set_aspect('equal')
    plt.axis('off')
    plt.show()

set_A = np.array([1, 2, 3])
set_B = np.array([3, 4, 5])
plot_venn_diagram(set_A, set_B)

def plot_equation():
    plt.figure()
    plt.text(0.5, 0.5, r"$A \cup B = B \cup A$", fontsize=20, ha='center', va='center')
    plt.gca().set_axis_off()
    plt.show()

plot_equation()

