import numpy as np
import pandas as pd
import plotly.express as px
import sympy as sp
import torch
from sklearn import datasets
from scipy import optimize
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Problem (a) and (b)
resistance_a = -400  # Invalid resistance
resistance_b = 500   # Valid resistance

if resistance_a < 0:
    result_a = "Invalid resistance"
else:
    result_a = "Valid resistance"

if resistance_b < 0:
    result_b = "Invalid resistance"
else:
    result_b = "Valid resistance"

# Problem (c)
R1, R2, Rs = sp.symbols('R1 R2 Rs')
equation = sp.Eq(Rs, R1 + R2)

# Assuming values for R1 and R2
R1_val = 300
R2_val = 200

# Solve for Rs
series_resistance = sp.solve(equation.subs({R1: R1_val, R2: R2_val}), Rs)[0]

# Visualization
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
R1_vals = np.linspace(0, 500, 50)
R2_vals = np.linspace(0, 500, 50)
R1_vals, R2_vals = np.meshgrid(R1_vals, R2_vals)
Rs_vals = R1_vals + R2_vals

ax.plot_surface(R1_vals, R2_vals, Rs_vals, cmap='viridis')
ax.set_xlabel('R1')
ax.set_ylabel('R2')
ax.set_zlabel('Rs')
plt.title('Series Resistance Comparison')
plt.show()

# PyTorch and scikit-learn example
# Assuming you have some random data
X, y = datasets.make_regression(n_samples=100, n_features=1, noise=10)

# PyTorch linear regression
model = torch.nn.Linear(1, 1)
criterion = torch.nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

for epoch in range(100):
    inputs = torch.from_numpy(X).float()
    targets = torch.from_numpy(y).float()

    optimizer.zero_grad()
    outputs = model(inputs)
    loss = criterion(outputs, targets)
    loss.backward()
    optimizer.step()

# Visualize the results
plt.scatter(X, y, label='Data')
plt.plot(X, model(torch.from_numpy(X).float()).detach().numpy(), color='red', label='Regression')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()
