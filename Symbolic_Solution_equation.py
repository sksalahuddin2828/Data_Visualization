import sympy as sp

# Define a symbolic variable
x = sp.Symbol('x')

# Solve equation: 3x + 5 = 12
equation = sp.Eq(3*x + 5, 12)
solution = sp.solve(equation, x)

print("Symbolic Solution:")
print(solution)

# Answer: Symbolic Solution: [7/3]
