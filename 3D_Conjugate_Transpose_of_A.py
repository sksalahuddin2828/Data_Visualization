import numpy as np
import pandas as pd
import sympy as sp

A = np.array([[1+2j, 3-4j, 5],
              [-6j, 7, 8+9j],
              [10, -11j, 12]])

A_conj_transpose = np.conj(A.T)
A_negation = -A

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_3d_matrix(matrix, title):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    rows, cols = matrix.shape
    x = np.arange(0, rows)
    y = np.arange(0, cols)
    x, y = np.meshgrid(x, y)
    z = np.real(matrix)

    ax.scatter(x, y, z, c=z.flatten(), cmap='viridis')
    ax.set_title(title)

    plt.show()

# Call the function for different matrices
plot_3d_matrix(A, 'Matrix A')
plot_3d_matrix(A_conj_transpose, 'Conjugate Transpose of A')
plot_3d_matrix(A_negation, 'Negation of A')

import plotly.graph_objects as go
import plotly.express as px

def plotly_3d_matrix(matrix, title):
    rows, cols = matrix.shape
    x = np.arange(0, rows)
    y = np.arange(0, cols)
    x, y = np.meshgrid(x, y)
    z = np.real(matrix)

    fig = px.scatter_3d(x=x.flatten(), y=y.flatten(), z=z.flatten(),
                        color=z.flatten(), title=title)
    fig.show()

# Call the function for different matrices
plotly_3d_matrix(A, 'Matrix A')
plotly_3d_matrix(A_conj_transpose, 'Conjugate Transpose of A')
plotly_3d_matrix(A_negation, 'Negation of A')

x, y, z, w = sp.symbols('x y z w')
skew_hermitian_formula = sp.Matrix([[0, x - sp.I*y, z],
                                   [x + sp.I*y, 0, w - sp.I*z],
                                   [z, w + sp.I*z, 0]])

sp.init_printing()
display(skew_hermitian_formula)
