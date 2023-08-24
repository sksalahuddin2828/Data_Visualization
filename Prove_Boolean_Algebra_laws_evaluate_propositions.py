import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from sympy import symbols, Eq, Not, And, Or

# Boolean Algebra Laws
def prove_boolean_algebra_laws():
    A, B = symbols('A B')
    
    commutative_law = Eq(A & B, B & A)
    associative_law = Eq((A & B) & B, A & (B & B))
    distributive_law = Eq(A & (B | B), (A & B) | (A & B))
    demorgans_law_1 = Eq(Not(A & B), Not(A) | Not(B))
    demorgans_law_2 = Eq(Not(A | B), Not(A) & Not(B))
    
    laws = [commutative_law, associative_law, distributive_law, demorgans_law_1, demorgans_law_2]
    
    for law in laws:
        print(f"Proving: {law}")
        proof = law.simplify()
        print("Proof:", proof)
        print("\n")

# Probability Calculation
def calculate_probability(favorable_outcomes, total_outcomes):
    return favorable_outcomes / total_outcomes

def evaluate_propositions():
    propositions = [
        "3 + 3 == 6",
        "2 * 2 == 4",
        "5 > 3",
        "'a' in ['a', 'e', 'i', 'o', 'u']"
    ]
    
    for proposition in propositions:
        statement = proposition
        result = eval(proposition)  # Evaluates the statement
        print(f"Proposition: {statement} is {result}")

# Induction Example
def prove_induction():
    n = symbols('n')
    proposition = Eq(n, 2 ** n)
    proof = proposition.simplify()
    print("Proof:", proof)

# Recursion Example
def recursive_function(n):
    if n == 0:
        return 5
    return recursive_function(n - 1) + 2

# Counting Example
def count_passwords():
    digits = ["2", "3", "4", "5", "7", "9"]
    total_passwords = len(digits) ** 3
    print("Total Passwords:", total_passwords)

# Run examples
prove_boolean_algebra_laws()
evaluate_propositions()
prove_induction()
print("Recursive Function:", recursive_function(3))
count_passwords()
