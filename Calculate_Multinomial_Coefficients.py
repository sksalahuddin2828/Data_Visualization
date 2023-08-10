from sympy import symbols, expand, binomial

# Define the variables
x, y, z = symbols('x y z')

# Define the expression
expression = (x + y + z)**3

# Expand the expression
expanded_expression = expand(expression)

# Print the expanded expression
print(expanded_expression)

x**3 + 3*x**2*y + 3*x**2*z + 3*x*y**2 + 6*x*y*z + 3*x*z**2 + y**3 + 3*y**2*z + 3*y*z**2 + z**3

# Calculate multinomial coefficients
def multinomial_coefficient(n, *k_values):
    numerator = binomial(n, sum(k_values))
    denominator = 1
    for k in k_values:
        denominator *= binomial(sum(k_values), k)
    return numerator // denominator

# Calculate and print coefficients for each term
terms = expanded_expression.as_ordered_terms()
for term in terms:
    variables = term.as_ordered_factors()
    k_values = [variables.count(var) for var in [x, y, z]]
    coefficient = multinomial_coefficient(3, *k_values)
    print(f"Coefficient for {term}: {coefficient}")



# Answer: x**3 + 3*x**2*y + 3*x**2*z + 3*x*y**2 + 6*x*y*z + 3*x*z**2 + y**3 + 3*y**2*z + 3*y*z**2 + z**3
#         Coefficient for x**3: 1
#         Coefficient for 3*x**2*y: 3
#         Coefficient for 3*x**2*z: 3
#         Coefficient for 3*x*y**2: 3
#         Coefficient for 6*x*y*z: 0
#         Coefficient for 3*x*z**2: 3
#         Coefficient for y**3: 1
#         Coefficient for 3*y**2*z: 3
#         Coefficient for 3*y*z**2: 3
#         Coefficient for z**3: 1
