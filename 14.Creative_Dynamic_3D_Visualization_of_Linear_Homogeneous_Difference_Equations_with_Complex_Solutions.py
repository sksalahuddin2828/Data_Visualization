import numpy as np
import plotly.graph_objects as go
import sympy as sp

# Define the symbolic variables
r, R = sp.symbols('r R')

# Define the recurrence relation (higher-order difference equation)
recurrence_relation = r**3 - 5*r**2 + 8*r - 4

# Solve for the roots of the characteristic equation
roots = sp.solve(recurrence_relation, r)

# Complex roots for increased complexity
complex_root1 = -1 + 2j
complex_root2 = -1 - 2j

# Define the initial conditions (more elaborate initial conditions)
a0 = 1
a1 = 2
a2 = 3

# Solve for C1, C2, and C3 using initial conditions
C3, C2, C1 = sp.symbols('C3 C2 C1')
eq1 = C3 * roots[0]**2 + C2 * roots[0] + C1 - a0
eq2 = C3 * roots[1]**2 + C2 * roots[1] + C1 - a1
eq3 = C3 * complex_root1**2 + C2 * complex_root1 + C1 - a2

C_values = sp.solve([eq1, eq2, eq3], (C3, C2, C1))

# Create the particular solution for the real part
real_particular_solution = C_values[C3] * roots[0]**r + C_values[C2] * roots[1]**r

# Create the particular solution for the complex part using sympy
complex_particular_solution = C_values[C3] * sp.exp(complex_root1 * R) + C_values[C2] * sp.exp(complex_root2 * R)

# Combine the real and complex parts of the particular solution
particular_solution = real_particular_solution + sp.re(complex_particular_solution)

# Convert the particular solution into a callable function
particular_solution_func = sp.lambdify((r, R), particular_solution, modules=['numpy', 'sympy'])

# Create meshgrid for 3D visualization
r_values = np.linspace(-5, 5, 100)
R_values = np.linspace(-5, 5, 100)
r, R = np.meshgrid(r_values, R_values)

# Evaluate the particular solution at each point
Z = particular_solution_func(r, R)

# Create 3D surface plot using Plotly
fig = go.Figure(data=[go.Surface(z=np.real(Z), x=r_values, y=R_values)])

# Customize the plot layout
fig.update_layout(scene=dict(
    xaxis_title='r',
    yaxis_title='R',
    zaxis_title='Value'
), title='Complex 3D Visualization of the Particular Solution using Plotly')

# Show the interactive 3D plot
fig.show()
