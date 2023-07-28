import numpy as np
import pandas as pd
import plotly.graph_objects as go
import scipy.stats as stats

# Sample data
n1, n2 = 100, 100
P1, P2 = 0.52, 0.47

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

# Display the probability
print(f"The probability that the survey will show a greater percentage of Republican voters in the second state than in the first state is: {probability:.2f}")

# Visualization using Plotly
x = np.linspace(-0.2, 0.2, 1000)
y = stats.norm.pdf(x, loc=mean_diff, scale=std_dev_diff)

fig = go.Figure()

# Probability Density Function
fig.add_trace(go.Scatter(x=x, y=y, mode='lines', line=dict(color='blue'), name='PDF'))

# Shaded area for the probability
fig.add_trace(go.Scatter(x=x, y=y, fill='tozeroy', fillcolor='green', name='P(Republican 2nd State > 1st State)',
                         hoverinfo='skip'))

fig.update_layout(
    title='Probability Distribution',
    xaxis_title='Difference in Proportions (p1 - p2)',
    yaxis_title='Probability Density',
    showlegend=False,
    plot_bgcolor='rgba(0, 0, 0, 0)'
)

fig.show()
