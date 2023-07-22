from sympy import symbols, diff, solve

# Define the variable symbol
x_sym = symbols('x')

# Define the function symbolically
y_sym = x_sym**2 + 3*x_sym

# Calculate the derivative
dy_dx_sym = diff(y_sym, x_sym)

# Find critical points (where dy/dx = 0)
critical_points = solve(dy_dx_sym, x_sym)

print("Critical Points:", critical_points)


# Answer: Critical Points: [-3/2]
