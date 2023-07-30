import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D

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

# Linear regression using numpy
b1 = correlation_coefficient * (data['Heating_Bills'].std() / data['Home_Size'].std())
b0 = data['Heating_Bills'].mean() - b1 * data['Home_Size'].mean()

# Define the regression line function
def regression_line(x):
    return b0 + b1 * x

# Create 3D animation of the mathematical dance
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Scatter plot of data points
ax.scatter(data['Home_Size'], data['Heating_Bills'], c='b', marker='o', label='Data')

# Plot the initial regression line
line, = ax.plot([], [], [], 'r-', label='Regression Line', lw=2)

# Function to update the regression line
def update_line(num):
    line.set_data(data['Home_Size'], data['Heating_Bills'])
    line.set_3d_properties(regression_line(data['Home_Size']))
    ax.set_title(f"Mathematical Dance: Step {num}/{len(data)}")

# Animate the regression line
from matplotlib.animation import FuncAnimation

num_steps = len(data)

ani = FuncAnimation(fig, update_line, frames=num_steps, repeat=False)

# Customize the plot appearance
ax.set_xlabel('Home Size (sq. feet)')
ax.set_ylabel('Heating Bills (dollars)')
ax.set_zlabel('Regression Line')
ax.set_title(f"Mathematical Dance: Step 0/{num_steps}")
ax.legend()

# Show the 3D animation
plt.show()
