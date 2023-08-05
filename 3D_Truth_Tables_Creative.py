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

# Creative Visualization for XOR and AND-OR
fig = go.Figure()

# Scatter plot for X ⨁ Y with custom marker symbols and colors
fig.add_trace(go.Scatter(x=X, y=Y, mode='markers', marker=dict(size=100, color='rgba(255, 100, 100, 0.7)', symbol='star'), name='X ⨁ Y'))

# Bar chart for (X ∧ ∼Y) ∨ (∼X ∧ Y) with color gradient based on the result
fig.add_trace(go.Bar(x=[f"(X={str(x)}, Y={str(y)})" for x, y in zip(X, Y)], y=result_AND_OR, marker=dict(color=result_AND_OR, colorbar=dict(title="Result", tickvals=[0, 1], ticktext=["False", "True"])), name='(X ∧ ∼Y) ∨ (∼X ∧ Y)'))

fig.update_layout(title="Creative Visualization: XOR and AND-OR", xaxis_title="X", yaxis_title="Y")
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

# Creative Visualization for XOR-NOR and NAND
fig2 = go.Figure()

# Bubble chart for (p ⨁ q) ∨ (p ↓ q) with bubble sizes based on the result
fig2.add_trace(go.Scatter(x=[f"(p={str(p)}, q={str(q)})" for p, q in zip(p, q)], y=result_XOR_NOR, mode='markers', marker=dict(size=result_XOR_NOR * 200, color=result_XOR_NOR, colorbar=dict(title="Result", tickvals=[0, 1], ticktext=["False", "True"])), name='(p ⨁ q) ∨ (p ↓ q)'))

# Funnel chart for p ↑ q with different colors for each category
fig2.add_trace(go.Funnel(x=result_NAND, y=[f"(p={str(p)}, q={str(q)})" for p, q in zip(p, q)], marker=dict(colorscale='Viridis'), name='p ↑ q'))

fig2.update_layout(title="Creative Visualization: XOR-NOR and NAND", xaxis_title="p", yaxis_title="q")
fig2.show()
