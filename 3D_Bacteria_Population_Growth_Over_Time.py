import plotly.graph_objects as go

# Population growth function
def population_growth(t):
    initial_population = 4000
    growth_rate = 1000
    population = initial_population + growth_rate * t
    return population

# Data for population growth
time_points = list(range(0, 11))  # Population at different time points (0 to 10 hours)
populations = [population_growth(t) for t in time_points]

# Create an interactive line plot
fig = go.Figure()
fig.add_trace(go.Scatter(x=time_points, y=populations, mode='lines+markers', name='Population'))
fig.update_layout(title='Bacteria Population Growth Over Time',
                  xaxis_title='Time (hours)',
                  yaxis_title='Population',
                  template='plotly_dark')
fig.show()
