import numpy as np
import pandas as pd
import sympy as sp
import matplotlib.pyplot as plt
import plotly.express as px

# Define symbolic variables
R3 = sp.Symbol('R3')
Rx = 100
R1 = 50.0
R2 = 175

# Create the equation
eq = sp.Eq(R1 * R3, R2 * Rx)

# Solve for R3
solution = sp.solve(eq, R3)
print(solution)

# Create a range of R3 values
R3_values = np.linspace(0, 200, 100)
bridge_values = (R2 * Rx) / (R1 + R2 + R3_values)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(R3_values, bridge_values, np.zeros_like(R3_values), label='Wheatstone Bridge')
ax.set_xlabel('R3 (Ω)')
ax.set_ylabel('Voltage (V)')
ax.set_zlabel('Z')
plt.legend()
plt.show()

df = pd.DataFrame({'R3 (Ω)': R3_values, 'Voltage (V)': bridge_values})

fig = px.scatter(df, x='R3 (Ω)', y='Voltage (V)', title='Wheatstone Bridge')
fig.show()
