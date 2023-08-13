import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sympy import symbols, Matrix, conjugate
from sympy.utilities.lambdify import lambdify
import plotly.graph_objects as go
from IPython.display import display, HTML

# Example: Hermitian Matrix Function
def hermitian_matrix(a, b, c, d):
    return np.array([[a, b + 1j * c], [b - 1j * c, d]])

# Example: Eigenvalues Calculation
def calculate_eigenvalues(matrix):
    eigenvalues = np.linalg.eigvals(matrix)
    return eigenvalues

# Example: Animated Eigenvalues Plot
def animated_eigenvalues_plot():
    t_vals = np.linspace(0, 2 * np.pi, 100)
    eigenvalues = [calculate_eigenvalues(hermitian_matrix(np.cos(t), np.sin(t), 0, 1)) for t in t_vals]

    fig = go.Figure()

    for eigenvalue in eigenvalues:
        fig.add_trace(go.Scatter(x=np.real(eigenvalue), y=np.imag(eigenvalue), mode='markers'))
    
    fig.update_layout(
        title="Animated Eigenvalues Plot",
        xaxis_title="Real Part",
        yaxis_title="Imaginary Part",
        showlegend=False
    )
    
    display(HTML(fig.to_html()))

# Example: Dynamic Explanation
dynamic_explanation = f"""
## Hermitian Matrix Properties

A Hermitian matrix has the following properties:

1. All diagonal elements are real numbers.
2. Non-diagonal elements contain complex numbers.
3. Eigenvalues are real.
4. ...

For a Hermitian matrix:

$$A = A^H$$

where $$A^H$$ is the conjugate transpose of matrix $$A$$.
"""

display(HTML(dynamic_explanation))

# Example: Mathematical Dance Animation (Using Matplotlib's Animation)
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

def animate(t):
    ax.clear()
    matrix = hermitian_matrix(np.cos(t), np.sin(t), 0, 1)
    ax.imshow(np.real(matrix), cmap='coolwarm')
    ax.set_title(f"Hermitian Matrix at t = {t:.2f}")

ani = FuncAnimation(fig, animate, frames=np.linspace(0, 2*np.pi, 50), interval=200)
plt.close(fig)
HTML(ani.to_jshtml())
