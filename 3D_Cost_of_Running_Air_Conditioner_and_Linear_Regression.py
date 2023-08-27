import numpy as np
import pandas as pd
import sympy as sp
import matplotlib.pyplot as plt
import plotly.express as px
import torch
import scipy.constants as const
from sklearn.linear_model import LinearRegression

# Given values
voltage = 408  # Volts
power = 50.0   # kW
time_per_day = 8.0  # hours
days_per_month = 30
electricity_cost = 0.09  # cents/kWh

# (a) Calculate effective resistance using P = V^2 / R
current = power / voltage
effective_resistance = voltage**2 / power

# (b) Calculate cost of running the air conditioner
total_power_consumed = power * time_per_day * days_per_month
total_cost = total_power_consumed * electricity_cost

# Print results
print("Effective Resistance:", effective_resistance, "Ohms")
print("Total Cost:", total_cost, "USD")

# Visualization: 3D Surface Plot of Cost vs. Time and Power
time_range = np.arange(0, 24, 0.5)
power_range = np.arange(0, 100, 5)
time_grid, power_grid = np.meshgrid(time_range, power_range)
cost_grid = time_grid * power_grid * electricity_cost

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(time_grid, power_grid, cost_grid, cmap='viridis')
ax.set_xlabel('Time (hours)')
ax.set_ylabel('Power (kW)')
ax.set_zlabel('Cost (USD)')
ax.set_title('Cost of Running Air Conditioner')
plt.show()

# Mathematical Dance: Visualization using Plotly
x = sp.Symbol('x')
y = sp.sin(x) * sp.exp(-0.1 * x)
expression = sp.lambdify(x, y, 'numpy')
x_vals = np.linspace(0, 10, 500)
y_vals = expression(x_vals)

df = pd.DataFrame({'x': x_vals, 'y': y_vals})
fig_dance = px.line(df, x='x', y='y', title='Mathematical Dance')
fig_dance.update_traces(line=dict(color='firebrick', width=2))
fig_dance.update_layout(xaxis_title='X-axis', yaxis_title='Y-axis')
fig_dance.show()

# Machine Learning: Linear Regression
np.random.seed(0)
X = np.random.rand(100, 1) * 10
y = 2 * X + 1 + np.random.randn(100, 1) * 2

model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

plt.scatter(X, y, label='Actual Data')
plt.plot(X, y_pred, color='red', label='Linear Regression')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear Regression')
plt.legend()
plt.show()
