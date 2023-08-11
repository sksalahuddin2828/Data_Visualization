import numpy as np
import matplotlib.pyplot as plt

# Plotting the linear equations
x_vals = np.linspace(-10, 10, 100)
y_eq1 = (19 - 4*x_vals) / 5
y_eq2 = 10*x_vals - 4

plt.plot(x_vals, y_eq1, label='4x + 5y = 19')
plt.plot(x_vals, y_eq2, label='5x - y/2 = 2')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.title('Linear Equations')
plt.show()
