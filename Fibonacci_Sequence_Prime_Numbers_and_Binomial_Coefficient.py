import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from sympy import symbols, Eq, Not, And, Or, factorial
from IPython.display import display, Markdown, Latex

# Boolean Algebra Laws
def prove_boolean_algebra_laws():
    A, B = symbols('A B')
    
    commutative_law = Eq(A & B, B & A)
    associative_law = Eq((A & B) & B, A & (B & B))
    distributive_law = Eq(A & (B | B), (A & B) | (A & B))
    demorgans_law_1 = Eq(Not(A & B), Not(A) | Not(B))
    demorgans_law_2 = Eq(Not(A | B), Not(A) & Not(B))
    
    laws = [commutative_law, associative_law, distributive_law, demorgans_law_1, demorgans_law_2]
    
    for idx, law in enumerate(laws, start=1):
        print(f"Law {idx}: {law}")
        proof = law.simplify()
        print("Proof:", proof)
        print("\n")

# Fibonacci Sequence using Recursion
def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Prime Number Generator
def generate_primes(limit):
    primes = []
    for num in range(2, limit + 1):
        is_prime = all(num % i != 0 for i in range(2, int(np.sqrt(num)) + 1))
        if is_prime:
            primes.append(num)
    return primes

# Binomial Coefficient Calculation
def binomial_coefficient(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

# Run examples
prove_boolean_algebra_laws()

n_terms = 10
fibonacci_sequence = [fibonacci_recursive(i) for i in range(n_terms)]
print("Fibonacci Sequence:", fibonacci_sequence)

primes_up_to_50 = generate_primes(50)
print("Prime Numbers up to 50:", primes_up_to_50)

n = 5
k = 2
binomial_result = binomial_coefficient(n, k)
print(f"Binomial Coefficient C({n}, {k}):", binomial_result)
