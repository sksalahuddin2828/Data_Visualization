import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Step 2: Data Generation (Optional)
# If required, generate synthetic data for visualization
# Example for a function: y = 2x^2 + 3x + 1
x_values = np.linspace(-5, 5, 100)
y_values = 2 * x_values ** 2 + 3 * x_values + 1

# Step 4: Mathematical Analysis
# Example: Solving an equation using sympy
x = sp.symbols('x')
equation = x**2 - 4
solutions = sp.solve(equation, x)

# Step 5: Data Visualization
# Example: 2D Line Plot using matplotlib
plt.plot(x_values, y_values)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of y = 2x^2 + 3x + 1')
plt.grid(True)
plt.show()

# Example: Interactive 3D Surface Plot using plotly
x_values_3d = np.linspace(-5, 5, 100)
y_values_3d = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x_values_3d, y_values_3d)
Z = 2 * X ** 2 + 3 * X + 1 + Y

fig = go.Figure(data=[go.Surface(z=Z, x=X, y=Y)])
fig.update_layout(title='3D Surface Plot of y = 2x^2 + 3x + 1 + z')
fig.show()

# Step 6: Machine Learning (Optional)
# If applicable, implement machine learning models for data analysis
from sklearn.linear_model import LinearRegression

# Using the synthetic data from Step 2 (x_values, y_values)
# Reshape the data for sklearn
X = x_values.reshape(-1, 1)
y = y_values

# Create and fit the linear regression model
model = LinearRegression()
model.fit(X, y)

# Get the coefficients of the linear regression line
slope = model.coef_[0]
intercept = model.intercept_

# Plot the synthetic data and the linear regression line
plt.scatter(X, y, label='Data')
plt.plot(X, model.predict(X), color='red', label='Linear Regression')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Regression Fit for y = 2x^2 + 3x + 1')
plt.legend()
plt.grid(True)
plt.show()

# For example, animate the linear regression line from Step 6
import matplotlib.animation as animation

def animate(i):
    line.set_ydata(model.predict(X) + 0.1 * i)
    return line,

fig, ax = plt.subplots()
ax.scatter(X, y, label='Data')
line, = ax.plot(X, model.predict(X), color='red', label='Linear Regression')

ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=True)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Animated Linear Regression Fit')
plt.grid(True)
plt.legend()

# Save the animation to a file (optional)
# ani.save('linear_regression_animation.gif', writer='pillow')

# Show the animation
plt.show()
