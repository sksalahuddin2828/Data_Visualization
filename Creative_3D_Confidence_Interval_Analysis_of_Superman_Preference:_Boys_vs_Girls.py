import numpy as np
import pandas as pd
import plotly.graph_objects as go

# Given data
n_boys = 400
n_girls = 300
p_boys = 0.40
p_girls = 0.30
confidence_level = 0.90

# Calculate the standard error and margin of error
SE = np.sqrt((p_boys * (1 - p_boys) / n_boys) + (p_girls * (1 - p_girls) / n_girls))
alpha = 1 - confidence_level
z_critical = stats.norm.ppf(1 - alpha / 2)
ME = z_critical * SE

# Calculate the confidence interval
lower_bound = p_boys - p_girls - ME
upper_bound = p_boys - p_girls + ME

# Generate some random points to visualize the confidence interval
num_points = 1000
boys_samples = np.random.binomial(n=n_boys, p=p_boys, size=num_points)
girls_samples = np.random.binomial(n=n_girls, p=p_girls, size=num_points)

# Calculate the difference in proportions for each sample
difference_samples = boys_samples / n_boys - girls_samples / n_girls

# Create a DataFrame to store the data
data = pd.DataFrame({
    "Boys": boys_samples,
    "Girls": girls_samples,
    "Difference": difference_samples
})

# Create the 3D scatter plot
fig = go.Figure()

# Add the scatter plot trace
fig.add_trace(go.Scatter3d(
    x=data["Boys"],
    y=data["Girls"],
    z=data["Difference"],
    mode='markers',
    marker=dict(
        size=5,
        color=data["Difference"],
        colorscale='Viridis',
        opacity=0.8,
        colorbar=dict(
            title="Difference",
            thickness=20
        ),
    ),
    name="Difference"
))

# Add confidence interval line using a custom shape
x_line = [n_boys, n_boys]
y_line = [n_girls, n_girls]
z_line = [lower_bound, upper_bound]

fig.add_trace(go.Scatter3d(
    x=x_line,
    y=y_line,
    z=z_line,
    mode='lines',
    line=dict(
        color='red',
        width=4,
    ),
    showlegend=False
))

# Set layout and axis labels
fig.update_layout(
    scene=dict(
        xaxis_title='Boys',
        yaxis_title='Girls',
        zaxis_title='Difference',
    ),
    width=600,
    height=600  # Adjust the width and height as per your preference
)

# Show the plot
fig.show()
