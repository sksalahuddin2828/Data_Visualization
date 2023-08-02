import numpy as np
import matplotlib.pyplot as plt

def recurrence_relation(x, h):
    return (4 * f(x + h) - 2 * f(x)) / 2

def f(x):
    return 1

x_values = np.linspace(-10, 10, 100)  # Define the range of x values
h = 0.1  # Define the value of h

f_values = [f(x) for x in x_values]
for i in range(2, len(x_values)):
    f_next = recurrence_relation(x_values[i], h)
    f_values.append(f_next)

plt.plot(x_values, f_values[:len(x_values)])  # Truncate f_values to have the same length as x_values
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Solution of the Recurrence Relation')
plt.show()
