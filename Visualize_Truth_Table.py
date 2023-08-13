import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sympy import symbols, Not, And, Or, Implies, Eq, simplify_logic
from sympy.logic.boolalg import truth_table

# Define symbolic variables
x, y, z = symbols('x y z')

# Define the propositions
propositions = [
    x & ~x,
    (x & (x >> y)) >> ~y,
    ((x >> y) & (y >> z)) & (x & ~z),
    ~(x >> y) | (~x | (x & y)),
    (x == z) >> (~y >> (x & z))
]

# Generate truth tables for propositions
def generate_truth_table(expression):
    tt = truth_table(expression, [x, y, z])
    return np.array([list(row) + [str(result)] for row, result in tt], dtype=object)

truth_tables = [generate_truth_table(prop) for prop in propositions]

# Convert truth tables to DataFrames
column_names = ['x', 'y', 'z', 'Result']
df_list = [pd.DataFrame(table, columns=column_names) for table in truth_tables]

# Visualize truth tables using Matplotlib
def visualize_truth_table(df, title):
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.axis('tight')
    ax.axis('off')
    ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')
    ax.set_title(title)
    plt.show()

for i, df in enumerate(df_list):
    visualize_truth_table(df, f"Proposition {i+1}")
