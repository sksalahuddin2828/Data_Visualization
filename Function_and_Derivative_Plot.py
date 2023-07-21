import numpy as np
import matplotlib.pyplot as plt

# Define the function f(x) = x^2 + 3x
def f(x):
    return x**2 + 3*x

# Define the derivative function f'(x) = 2x + 3
def f_derivative(x):
    return 2*x + 3

# Generate x values for plotting
x_values = np.linspace(-5, 5, 100)

# Calculate the corresponding y values for f(x) and f'(x)
y_values = f(x_values)
y_derivative_values = f_derivative(x_values)

# Create a dynamic plot
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the original function f(x) in blue
ax.plot(x_values, y_values, label='f(x) = x^2 + 3x', color='blue')

# Plot the derivative function f'(x) in red
ax.plot(x_values, y_derivative_values, label="f'(x) = 2x + 3", color='red')

# Mark the points where f'(x) = 0 (critical points)
critical_points_x = -3/2
critical_points_y = f(critical_points_x)
ax.scatter(critical_points_x, critical_points_y, color='green', s=100, label='Critical Points')

# Add labels and title
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Function and Its Derivative')
ax.axhline(0, color='black', lw=0.5)
ax.axvline(0, color='black', lw=0.5)

# Add a legend
ax.legend()

# Show the plot
plt.grid()
plt.show()
