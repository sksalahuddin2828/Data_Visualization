import plotly.express as px

# Sample data
currents = [1, 2, 3, 4, 5]
powers = [20, 45, 70, 95, 120]

# Create a line plot
fig = px.line(x=currents, y=powers, title="Average Power vs. Current")
fig.update_xaxes(title="Current")
fig.update_yaxes(title="Average Power")

# Show the plot
fig.show()
