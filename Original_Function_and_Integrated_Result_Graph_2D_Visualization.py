import numpy as np
import matplotlib.pyplot as plt

# Define values for 'a' and 'c'
a_val = 1.5
c_val = 2.0

# Define x values
x_values = np.linspace(0, 2, 400)

# Calculate the integrated result
integrated_result = (1 / a_val) * np.exp(a_val * x_values) + c_val

# Create the plot
plt.figure(figsize=(10, 6))

# Plot the original function
plt.plot(x_values, np.exp(a_val * x_values), label='Original Function: $e^{ax}$')

# Plot the integrated result
plt.plot(x_values, integrated_result, label='Integrated Result: $\\frac{1}{a} e^{ax} + c$')

# Add labels and legend
plt.xlabel('x')
plt.ylabel('y')
plt.title('Integration and Result Visualization')
plt.legend()

# Add annotations
plt.annotate('Original Function', (0.5, np.exp(0.5 * a_val)), textcoords="offset points", xytext=(20,10), ha='center')
plt.annotate('Integrated Result', (1.5, integrated_result[300]), textcoords="offset points", xytext=(-40,-30), ha='center')

# Show the plot
plt.show()
