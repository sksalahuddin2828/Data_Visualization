import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import plotly.graph_objects as go
import sympy as sp

# Data for school A
mean_A = 1000
std_dev_A = 100
sample_size_A = 15

# Data for school B
mean_B = 950
std_dev_B = 90
sample_size_B = 20

# Confidence level
confidence_level = 0.90

# Calculate standard error
se = np.sqrt((std_dev_A ** 2) / sample_size_A + (std_dev_B ** 2) / sample_size_B)

# Calculate degrees of freedom
df = sample_size_A + sample_size_B - 2

# Calculate t critical value
t_critical = stats.t.ppf((1 + confidence_level) / 2, df)

# Calculate margin of error
margin_of_error = t_critical * se

# Calculate the difference in means
mean_difference = mean_A - mean_B

# Calculate the lower and upper bounds of the confidence interval
lower_bound = mean_difference - margin_of_error
upper_bound = mean_difference + margin_of_error

# Additional mathematical expressions and functions
x, y = sp.symbols('x y')
expression = sp.sin(x) + sp.log(y)

# Convert the expression to a numerical function using lambdify
numerical_expression = sp.lambdify([x, y], expression, 'numpy')

# Create data for the additional mathematical plot
plot_range = np.linspace(-2 * np.pi, 2 * np.pi, 100)
expression_values = numerical_expression(plot_range, plot_range)

# Create a pandas DataFrame to store the data
data = {
    'School': ['A', 'B'],
    'Mean': [mean_A, mean_B],
    'Sample Size': [sample_size_A, sample_size_B]
}
df = pd.DataFrame(data)

# Create a bar plot to compare means
plt.figure(figsize=(8, 6))
plt.bar(df['School'], df['Mean'], yerr=[1.96 * (std_dev_A / np.sqrt(sample_size_A)), 1.96 * (std_dev_B / np.sqrt(sample_size_B))], capsize=5)
plt.ylabel('Mean Test Score')
plt.title('Comparison of Test Scores between School A and School B')

# Additional mathematical plot
plt.figure(figsize=(8, 6))
plt.plot(plot_range, expression_values)
plt.xlabel('x')
plt.ylabel('Expression Value')
plt.title('Plot of Expression: sin(x) + log(y)')

# Create a 3D surface plot for the mathematical expression using Plotly
X, Y = np.meshgrid(plot_range, plot_range)
Z = numerical_expression(X, Y)

fig = go.Figure(data=[go.Surface(z=Z, x=X, y=Y)])
fig.update_layout(title="3D Surface Plot of Expression: sin(x) + log(y)",
                  scene=dict(xaxis_title="x", yaxis_title="y", zaxis_title="Expression Value"),
                  height=600, width=800)

# Show all plots
plt.show()
fig.show()
