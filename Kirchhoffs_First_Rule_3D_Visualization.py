import sympy as sp
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Define symbolic variables
I1, I2, I3 = sp.symbols('I1 I2 I3')

# Kirchhoff's first rule equation: I1 = I2 + I3
equation = sp.Eq(I1, I2 + I3)

# Solve the equation symbolically
solution = sp.solve(equation, I3)

# Create a function to calculate I3 for given values of I1 and I2
calculate_I3 = sp.lambdify((I1, I2), solution[0])

# Define a range of I1 and I2 values
I1_values = np.linspace(0, 10, 100)
I2_values = np.linspace(0, 10, 100)

# Calculate I3 for the entire range
I3_values = np.zeros((len(I1_values), len(I2_values)))

for i, I1_val in enumerate(I1_values):
    for j, I2_val in enumerate(I2_values):
        I3_values[i, j] = calculate_I3(I1_val, I2_val)

# Create a DataFrame to store the results
df = pd.DataFrame(I3_values, index=I1_values, columns=I2_values)

# Create a 2D heatmap using Plotly
fig = px.imshow(df,
                labels={'index': 'I1 (A)', 'columns': 'I2 (A)', 'color': 'I3 (A)'},
                title='Kirchhoff\'s First Rule Visualization',
                x=I2_values,
                y=I1_values,
                color_continuous_scale='Viridis')

fig.update_xaxes(type='linear')
fig.update_yaxes(type='linear')
fig.show()

# Create a 3D surface plot using Matplotlib
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
I1_grid, I2_grid = np.meshgrid(I1_values, I2_values)
ax.plot_surface(I1_grid, I2_grid, I3_values.T, cmap='viridis')
ax.set_xlabel('I1 (A)')
ax.set_ylabel('I2 (A)')
ax.set_zlabel('I3 (A)')
ax.set_title('3D Visualization of Kirchhoff\'s First Rule')
plt.show()
