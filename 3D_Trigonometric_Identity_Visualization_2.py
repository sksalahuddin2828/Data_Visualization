import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

theta_vals = np.linspace(0, 2 * np.pi, 100)
cos_squared_vals = np.cos(theta_vals)**2
sin_squared_vals = np.sin(theta_vals)**2
two_cos_squared_minus_one_vals = 2 * cos_squared_vals - 1

data = {'Theta': theta_vals,
        'cos^2(θ)': cos_squared_vals,
        'sin^2(θ)': sin_squared_vals,
        '2cos^2(θ) - 1': two_cos_squared_minus_one_vals}

df = pd.DataFrame(data)
print(df.head())

plt.figure(figsize=(10, 6))
plt.plot(theta_vals, cos_squared_vals, label='$cos^2(θ)$')
plt.plot(theta_vals, sin_squared_vals, label='$sin^2(θ)$')
plt.plot(theta_vals, two_cos_squared_minus_one_vals, label='$2cos^2(θ) - 1$')

plt.xlabel('θ')
plt.ylabel('Value')
plt.title('Trigonometric Identity Visualization')
plt.legend()
plt.grid(True)
plt.show()
