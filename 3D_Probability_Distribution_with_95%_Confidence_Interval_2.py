import numpy as np
import pandas as pd
import plotly.graph_objects as go
import scipy.stats as stats
import sympy as sp
from sympy.utilities import lambdify

# Sample data
n1, n2 = 100, 100
P1, P2 = 0.52, 0.47
alpha = 0.05  # Significance level for confidence intervals

# Step 1: Check if the sample size is large enough
assert n1 * P1 >= 10 and n1 * (1 - P1) >= 10, "Sample size for the first state is not large enough."
assert n2 * P2 >= 10 and n2 * (1 - P2) >= 10, "Sample size for the second state is not large enough."

# Step 2: Calculate the mean of the difference in sample proportions
mean_diff = P1 - P2

# Step 3: Calculate the standard deviation of the difference
std_dev_diff = np.sqrt((P1 * (1 - P1) / n1) + (P2 * (1 - P2) / n2))

# Step 4: Calculate the probability using the z-score
z_score = (0 - mean_diff) / std_dev_diff
probability = stats.norm.cdf(z_score)

# Step 5: Calculate the confidence intervals
margin_of_error = stats.norm.ppf(1 - alpha / 2) * std_dev_diff
lower_bound = mean_diff - margin_of_error
upper_bound = mean_diff + margin_of_error

# Display the results
print(f"The probability that the survey will show a greater percentage of Republican voters in the second state than in the first state is: {probability:.2f}")
print(f"Confidence Interval (95%): {lower_bound:.3f} to {upper_bound:.3f}")

# Symbolic calculations with SymPy
x = sp.Symbol('x')
pdf = sp.exp(-0.5 * ((x - mean_diff) / std_dev_diff)**2) / (std_dev_diff * sp.sqrt(2 * sp.pi))
mean_diff_sym = sp.Rational(P1, 1) - sp.Rational(P2, 1)

# Calculate the cumulative distribution function (CDF) symbolically
cdf_sym = sp.integrate(pdf, (x, -sp.oo, mean_diff_sym)) 

# Calculate the quantile for the standard normal distribution
z_quantile = sp.erfinv(1 - alpha / 2)

# Evaluate the CDF and quantile as floating-point numbers
probability_val = round(cdf_sym.evalf(), 2)
lower_bound_val = round((mean_diff_sym - z_quantile * std_dev_diff).evalf(), 3)
upper_bound_val = round((mean_diff_sym + z_quantile * std_dev_diff).evalf(), 3)

# Display the symbolic results
print(f"Symbolic probability: {probability_val:.2f}")
print(f"Symbolic confidence interval (95%): {lower_bound_val:.3f} to {upper_bound_val:.3f}")

# Visualization using Plotly
x_values = np.linspace(-0.2, 0.2, 1000)
y_values = stats.norm.pdf(x_values, loc=mean_diff, scale=std_dev_diff)

fig = go.Figure()

# Probability Density Function
fig.add_trace(go.Scatter(x=x_values, y=y_values, mode='lines', line=dict(color='blue'), name='PDF'))

# Shaded area for the probability
fig.add_trace(go.Scatter(x=x_values, y=y_values, fill='tozeroy', fillcolor='green', name='P(Republican 2nd State > 1st State)', 
                         hoverinfo='skip'))

# Confidence Intervals
fig.add_trace(go.Scatter(x=[float(lower_bound_val), float(upper_bound_val)], y=[0, 0], mode='lines', line=dict(color='red', dash='dash'),
                         name='Confidence Interval (95%)'))

fig.update_layout(
    title='Probability Distribution with 95% Confidence Interval',
    xaxis_title='Difference in Proportions (p1 - p2)',
    yaxis_title='Probability Density',
    showlegend=True,
    plot_bgcolor='rgba(0, 0, 0, 0)'
)

fig.show()
