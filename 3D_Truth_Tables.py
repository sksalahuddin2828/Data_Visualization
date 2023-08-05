import numpy as np
import pandas as pd
import plotly.graph_objects as go

# Helper function to create truth tables
def create_truth_table(propositions, operation):
    n = len(propositions)
    m = 2 ** n
    truth_table = np.zeros((m, n + 1), dtype=int)
    for i in range(n):
        truth_table[:, i] = (np.arange(m) // (2 ** i)) % 2
    truth_table[:, n] = operation(*[truth_table[:, i] for i in range(n)]).astype(int)
    return truth_table

# 1. Prove that X ⨁ Y ≅ (X ∧ ∼Y) ∨ (∼X ∧ Y).
X = np.array([True, True, False, False])
Y = np.array([True, False, True, False])

result_XOR = X ^ Y
result_AND_OR = (X & ~Y) | (~X & Y)

are_equivalent = np.array_equal(result_XOR, result_AND_OR)

print("Truth Table for X ⨁ Y:")
print(pd.DataFrame({"X": X, "Y": Y, "X ⨁ Y": result_XOR}))

print("\nTruth Table for (X ∧ ∼Y) ∨ (∼X ∧ Y):")
print(pd.DataFrame({"X": X, "Y": Y, "(X ∧ ∼Y) ∨ (∼X ∧ Y)": result_AND_OR}))

print("\nAre the expressions equivalent?", are_equivalent)

# Visualization for X ⨁ Y and (X ∧ ∼Y) ∨ (∼X ∧ Y)
fig = go.Figure()

# Scatter plot for X ⨁ Y
fig.add_trace(go.Scatter(x=X, y=Y, mode='markers', marker=dict(size=20, color='blue'), name='X ⨁ Y'))

# Scatter plot for (X ∧ ∼Y) ∨ (∼X ∧ Y)
fig.add_trace(go.Scatter(x=result_AND_OR, y=result_AND_OR, mode='markers', marker=dict(size=20, color='red'), name='(X ∧ ∼Y) ∨ (∼X ∧ Y)'))

fig.update_layout(title="XOR and AND-OR Visualization", xaxis_title="X", yaxis_title="Y")
fig.show()

# 2. Show that (p ⨁ q) ∨ (p ↓ q) is equivalent to p ↑ q.
p = np.array([True, True, False, False])
q = np.array([True, False, True, False])

result_XOR_NOR = (p ^ q) | ~(p | q)
result_NAND = ~(p & q)

are_equivalent = np.array_equal(result_XOR_NOR, result_NAND)

print("\nTruth Table for (p ⨁ q) ∨ (p ↓ q):")
print(pd.DataFrame({"p": p, "q": q, "(p ⨁ q) ∨ (p ↓ q)": result_XOR_NOR}))

print("\nTruth Table for p ↑ q:")
print(pd.DataFrame({"p": p, "q": q, "p ↑ q": result_NAND}))

print("\nAre the expressions equivalent?", are_equivalent)

# Visualization for (p ⨁ q) ∨ (p ↓ q) and p ↑ q
fig2 = go.Figure()

# Scatter plot for (p ⨁ q) ∨ (p ↓ q)
fig2.add_trace(go.Scatter(x=result_XOR_NOR, y=result_XOR_NOR, mode='markers', marker=dict(size=20, color='green'), name='(p ⨁ q) ∨ (p ↓ q)'))

# Scatter plot for p ↑ q
fig2.add_trace(go.Scatter(x=result_NAND, y=result_NAND, mode='markers', marker=dict(size=20, color='purple'), name='p ↑ q'))

fig2.update_layout(title="XOR-NOR and NAND Visualization", xaxis_title="p", yaxis_title="q")
fig2.show()
