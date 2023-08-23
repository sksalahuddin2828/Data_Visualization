import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact

# Define the function
def quadratic_function(a, b, c):
    x = np.linspace(-10, 10, 400)
    y = a * x**2 + b * x + c
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Quadratic Function: ax^2 + bx + c')

# Create interactive widget
interact(quadratic_function, a=(-2, 2, 0.1), b=(-5, 5, 0.1), c=(-10, 10, 0.1))
