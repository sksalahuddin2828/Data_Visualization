import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sympy as sp

# Generate some example data for home size and heating bills
np.random.seed(42)
home_size = np.random.randint(1000, 5000, 50)
heating_bills = home_size * 0.7 + np.random.normal(loc=0, scale=500, size=50)

# Create a pandas DataFrame
data = pd.DataFrame({'Home_Size': home_size, 'Heating_Bills': heating_bills})

# Calculate the correlation coefficient (r)
correlation_coefficient = data['Home_Size'].corr(data['Heating_Bills'])

# Calculate the coefficient of determination (R2)
coefficient_of_determination = correlation_coefficient**2

# Print the results
print(f"Correlation Coefficient (r): {correlation_coefficient}")
print(f"Coefficient of Determination (R2): {coefficient_of_determination}")

# Linear regression using Sympy to find the equation of the regression line
x, y = sp.symbols('x y')
b1 = correlation_coefficient * (data['Heating_Bills'].std() / data['Home_Size'].std())
b0 = data['Heating_Bills'].mean() - b1 * data['Home_Size'].mean()
regression_equation = sp.Eq(y, b0 + b1 * x)
print("Regression Equation:")
print(regression_equation)

# Visualize the data and regression line in a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(data['Home_Size'], data['Heating_Bills'], c='b', marker='o', label='Data')
ax.set_xlabel('Home Size (sq. feet)')
ax.set_ylabel('Heating Bills (dollars)')
ax.set_zlabel('Regression Line')
ax.set_title('Linear Regression')
ax.plot(data['Home_Size'], b0 + b1 * data['Home_Size'], 'r-', label='Regression Line')
ax.legend()

plt.show()
