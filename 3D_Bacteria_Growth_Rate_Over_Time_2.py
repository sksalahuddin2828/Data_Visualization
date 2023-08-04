import pandas as pd
import plotly.express as px

# Load the data from the CSV file
data = pd.read_csv("bacteria_population.csv")

# Calculate the growth rate using pandas (assuming it's exponential growth)
data['Growth_Rate'] = data['Population'].pct_change()

# Plot the bacteria population over time
fig1 = px.line(data, x='Time (hours)', y='Population', title='Bacteria Population Over Time',
               template='plotly_dark')
fig1.show()

# Plot the growth rate over time
fig2 = px.line(data, x='Time (hours)', y='Growth_Rate', title='Bacteria Growth Rate Over Time',
               template='plotly_dark')
fig2.show()
