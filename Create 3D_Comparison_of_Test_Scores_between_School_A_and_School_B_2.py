import plotly.graph_objects as go

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

# Create the data for the 3D bar chart
data = [
    go.Bar(
        x=['A'],
        y=[mean_A],
        name='School A',
        error_y=dict(
            type='data',
            array=[margin_of_error],
            visible=True
        )
    ),
    go.Bar(
        x=['B'],
        y=[mean_B],
        name='School B',
    )
]

# Create the layout
layout = go.Layout(
    scene=dict(
        xaxis=dict(title='School'),
        yaxis=dict(title='Mean Test Score'),
        zaxis=dict(title='Confidence Interval'),
        xaxis_tickvals=[0, 1],
        xaxis_ticktext=['A', 'B']
    ),
    title="Comparison of Test Scores between School A and School B",
    height=600,
    width=800
)

# Create the figure and show the plot
fig = go.Figure(data=data, layout=layout)
fig.show()
