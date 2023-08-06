import numpy as np
import pandas as pd
import sympy as sp
import matplotlib.pyplot as plt

# Define the universe U (e.g., integers from -5 to 5)
U = np.arange(-5, 6)

# Define the proposition p(x)
x = sp.Symbol('x')
p = x**2 - 4

# Evaluate the proposition for each value of x in the universe U
propositions = [p.subs(x, val) for val in U]

# Create a DataFrame to represent the propositions for each value of x
df = pd.DataFrame({'x': U, 'p(x)': propositions})

# Filter the values of x where the proposition p(x) is true
true_propositions = df[df['p(x)'] > 0]

# Create a beautiful 3D visualization using matplotlib
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the true propositions in green and the false propositions in red
ax.scatter(true_propositions['x'], true_propositions['p(x)'], zs=0, s=50, c='g', marker='o', label='True')
ax.scatter(df[df['p(x)'] <= 0]['x'], df[df['p(x)'] <= 0]['p(x)'], zs=0, s=50, c='r', marker='o', label='False')

ax.set_xlabel('x')
ax.set_ylabel('p(x)')
ax.set_zlabel('Truth Value')
ax.set_title('3D Visualization of Propositions with Existential Quantifier')
ax.legend()
plt.show()
