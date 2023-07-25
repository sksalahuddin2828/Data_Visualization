import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

n_values = np.arange(6, 100, 1)  # You can adjust the range based on your requirements

log_equation = lambda n: np.prod([np.log(i+1) for i in range(2, n+1)]) - 10
solutions = [n for n in n_values if np.abs(log_equation(n)) < 0.001]

if len(solutions) > 0:
    n = solutions[0]
    print(f"The value of n is: {n}")
else:
    print("No solution found in the given range.")

n_values = np.arange(6, 100, 1)  # You can adjust the range based on your requirements

log_equation = lambda n: np.prod([np.log(i+1) for i in range(2, n+1)]) - 10
solutions = [n for n in n_values if np.abs(log_equation(n)) < 0.001]

if len(solutions) > 0:
    n = solutions[0]
    print(f"The value of n is: {n}")
else:
    print("No solution found in the given range.")

# Prepare the data
log_values = [np.prod([np.log(i+1) for i in range(2, n+1)]) for n in n_values]

# Create 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(n_values, log_values, np.zeros_like(n_values), c='r', marker='o')
ax.set_xlabel('n')
ax.set_ylabel('log equation value')
ax.set_zlabel('Zero Line')
ax.set_title('3D Visualization of log equation')
plt.show()
