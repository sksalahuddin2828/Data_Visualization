import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import plotly.graph_objects as go
import sympy as sp

# Data for men
mean_men = 20
std_dev_men = 3
sample_size_men = 500

# Data for women
mean_women = 15
std_dev_women = 2
sample_size_women = 1000

# Confidence level
confidence_level = 0.99

# Calculate standard error
se = np.sqrt((std_dev_men ** 2) / sample_size_men + (std_dev_women ** 2) / sample_size_women)

# Calculate degrees of freedom
df = sample_size_men + sample_size_women - 2

# Calculate t critical value (since the sample sizes are large enough, we use z-score approximation)
t_critical = stats.norm.ppf((1 + confidence_level) / 2)

# Calculate margin of error
margin_of_error = t_critical * se

# Calculate the difference in means
mean_difference = mean_men - mean_women

# Calculate the lower and upper bounds of the confidence interval
lower_bound = mean_difference - margin_of_error
upper_bound = mean_difference + margin_of_error

# Additional mathematical expressions and functions
x, y = sp.symbols('x y')
expression_1 = sp.sin(x) + sp.log(y)
expression_2 = sp.exp(-x) * sp.cos(y)

# Convert the expressions to numerical functions using lambdify
numerical_expression_1 = sp.lambdify([x, y], expression_1, 'numpy')
numerical_expression_2 = sp.lambdify([x, y], expression_2, 'numpy')

# Generate additional data points for the 3D plot
x_values = np.linspace(mean_men - 3 * std_dev_men, mean_men + 3 * std_dev_men, 100)
y_values = np.linspace(mean_women - 3 * std_dev_women, mean_women + 3 * std_dev_women, 100)
X, Y = np.meshgrid(x_values, y_values)

# Calculate the Z values (difference in means) for the 3D plot
Z = X - Y

# Create a pandas DataFrame to store the data
data = {
    'Group': ['Men', 'Women'],
    'Mean': [mean_men, mean_women],
    'Sample Size': [sample_size_men, sample_size_women]
}
df = pd.DataFrame(data)

# Create a bar plot to compare means
plt.figure(figsize=(8, 6))
colors = ['blue', 'orange']
plt.bar(df['Group'], df['Mean'], yerr=[margin_of_error, margin_of_error], capsize=5, color=colors)
plt.ylabel('Average Expenditure', fontsize=12)
plt.title('Comparison of Average Expenditure between Men and Women', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='y', linestyle='--')

# Additional mathematical plot with artistic touches
plt.figure(figsize=(8, 6))
plt.plot(x_values, numerical_expression_1(x_values, x_values), label='sin(x) + log(y)', color='purple', linewidth=2)
plt.plot(x_values, numerical_expression_2(x_values, x_values), label='exp(-x) * cos(y)', color='green', linewidth=2)
plt.fill_between(x_values, numerical_expression_1(x_values, x_values), numerical_expression_2(x_values, x_values), color='lavender')
plt.xlabel('x', fontsize=14)
plt.ylabel('Expression Value', fontsize=14)
plt.title('Plot of Mathematical Expressions', fontsize=16)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.legend(fontsize=12)
plt.grid(linestyle='--')

# Create a 3D surface plot for the spending difference using Plotly
fig = go.Figure()
fig.add_trace(go.Surface(z=Z, x=X, y=Y, colorscale='Viridis'))

# Add the means for men and women with error bars
fig.add_trace(go.Scatter3d(x=[mean_men], y=[mean_women], z=[mean_difference],
                           mode='markers', marker=dict(size=5, color='red'), name='Means'))
fig.add_trace(go.Scatter3d(x=[mean_men, mean_men], y=[mean_women, mean_women],
                           z=[lower_bound, upper_bound], mode='lines', line=dict(color='black'),
                           name='Confidence Interval'))

fig.update_layout(title="Spending Difference between Men and Women",
                  scene=dict(xaxis_title="Men Spending", yaxis_title="Women Spending", zaxis_title="Difference"),
                  height=600, width=800)

# Show all plots
plt.show()
fig.show()
