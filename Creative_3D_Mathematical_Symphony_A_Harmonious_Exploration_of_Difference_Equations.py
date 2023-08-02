import numpy as np
import plotly.graph_objects as go
import sympy as sp

# Define the variables and constants
r = sp.symbols('r')
C1, C2 = sp.symbols('C1 C2')

# Define the characteristic equation
recurrence_relation = r**2 - 4*r + 4

# Find the characteristic roots
roots = sp.solve(recurrence_relation, r)
print("Roots of the equation:", roots)

# Define the homogeneous solution
homogeneous_solution = C1 * 2**r + C2 * r * 2**r

# Define the initial conditions
a0 = 0
a1 = 6

# Substitute the initial conditions to find C1 and C2
C_values = sp.solve([homogeneous_solution.subs(r, 0) - a0, homogeneous_solution.subs(r, 1) - a1], [C1, C2])
C1_value = C_values[C1]
C2_value = C_values[C2]

# Define the particular solution
particular_solution = (1 + 2*r) * 2**r

# Combine the homogeneous and particular solutions
solution = homogeneous_solution.subs({C1: C1_value, C2: C2_value}) + particular_solution

# Convert the solution into a callable function
solution_func = sp.lambdify(r, solution, 'numpy')

# Create a range of values for r
r_values = np.linspace(0, 10, 100)

# Evaluate the solution at each point and extract real and imaginary parts
a_values = np.array([sp.re(solution_func(r_val)) for r_val in r_values])
b_values = np.array([sp.im(solution_func(r_val)) for r_val in r_values])

# Convert the values to Python floats
a_values = a_values.astype(float)
b_values = b_values.astype(float)

# Create the 3D plot using Plotly
fig = go.Figure(data=go.Scatter3d(x=r_values, y=a_values, z=b_values, mode='lines'))
fig.update_layout(title='3D Visualization of the Solution', scene=dict(
    xaxis=dict(title='r'),
    yaxis=dict(title='Real Part'),
    zaxis=dict(title='Imaginary Part'),
))
fig.show()
