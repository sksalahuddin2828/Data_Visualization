import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the Function to Integrate
def function_to_integrate(x, a):
    return np.sin(2*a*x)**2

# Generate Data for Visualization
a_vals = np.linspace(0.1, 2*np.pi, 100)  # Avoid a=0 for division
results = []
expected_results = []
for a_val in a_vals:
    integral_result = np.trapz(function_to_integrate(x_vals, a_val), x_vals)
    expected_result = a_val**2 - np.sin(2*a_val)**2 / (4*a_val)
    results.append(integral_result)
    expected_results.append(expected_result)

df = pd.DataFrame({'a': a_vals, 'result': results, 'expected_result': expected_results})

# Matplotlib 3D Visualization
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(df['a'], df['result'], df['expected_result'])
ax.set_xlabel('a')
ax.set_ylabel('Integral Result')
ax.set_zlabel('Expected Result')
plt.show()
