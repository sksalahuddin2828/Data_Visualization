import numpy as np
import sympy as sp
from scipy.optimize import fsolve

# Define the variables
emf_standard_cell = 12.0  # V
Rx = 5.000  # Ω
Rs = 2.500  # Ω

# Define the unknown EMF as a symbol
emf_cell = sp.symbols('emf_cell')

# Define the balance equation for the potentiometer
balance_equation = emf_cell * Rs / (Rx + Rs) - emf_standard_cell

# Convert the SymPy expression into a callable function
balance_equation_func = sp.lambdify(emf_cell, balance_equation)

# Solve for the unknown EMF using fsolve from scipy
emf_solution = fsolve(balance_equation_func, emf_standard_cell)

# Extract the solution (EMF of the cell)
emf_of_cell = emf_solution[0]

print(f"The EMF of the cell is {emf_of_cell:.2f} V")

# Answer: The EMF of the cell is 36.00 V


import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import sympy as sp
from scipy.optimize import fsolve

# Define the variables
emf_standard_cell = 12.0  # V
Rx_values = np.linspace(0.1, 10, 100)  # Create an array of Rx values
Rs_values = np.linspace(0.1, 10, 100)  # Create an array of Rs values

# Create a meshgrid of Rx and Rs values
Rx_mesh, Rs_mesh = np.meshgrid(Rx_values, Rs_values)

# Define the function to calculate EMF for a given Rx and Rs
def calculate_emf(emf_cell, Rx, Rs):
    return emf_cell * Rs / (Rx + Rs) - emf_standard_cell

# Calculate EMF for each combination of Rx and Rs
emf_values = calculate_emf(emf_standard_cell, Rx_mesh, Rs_mesh)

# Create a DataFrame for visualization
df = pd.DataFrame({
    'Rx': Rx_mesh.flatten(),
    'Rs': Rs_mesh.flatten(),
    'EMF': emf_values.flatten()
})

# Create a 3D surface plot using Plotly
fig = go.Figure(data=[go.Surface(z=emf_values, x=Rx_mesh, y=Rs_mesh)])
fig.update_layout(
    title='EMF of the Cell vs. Rx and Rs',
    scene=dict(
        xaxis_title='Rx (Ω)',
        yaxis_title='Rs (Ω)',
        zaxis_title='EMF (V)',
    )
)

# Show the interactive Plotly plot
fig.show()
