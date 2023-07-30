import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Generate some example data for home size and heating bills
np.random.seed(42)
home_size = np.random.randint(1000, 5000, 50)
heating_bills = home_size * 0.7 + np.random.normal(loc=0, scale=500, size=50)

# Create a pandas DataFrame
data = pd.DataFrame({'Home_Size': home_size, 'Heating_Bills': heating_bills})

# Calculate the correlation coefficient (r)
correlation_coefficient = data['Home_Size'].corr(data['Heating_Bills'])

# Calculate the coefficient of determination (R2)
coefficient_of_determination = correlation_coefficient ** 2

# Linear regression using numpy
b1 = correlation_coefficient * (data['Heating_Bills'].std() / data['Home_Size'].std())
b0 = data['Heating_Bills'].mean() - b1 * data['Home_Size'].mean()

# Define the regression line function
def regression_line(x):
    return b0 + b1 * x

# Create a 3D plot
fig = make_subplots(rows=1, cols=1, specs=[[{'type': 'scatter3d'}]])
fig.update_layout(scene=dict(
                    xaxis_title='Home Size (sq. feet)',
                    yaxis_title='Heating Bills (dollars)',
                    zaxis_title='Regression Line'),
                    title=f"Mathematical Dance: Step 0/{len(data)}")

# Scatter plot of data points
scatter_data = go.Scatter3d(
    x=data['Home_Size'],
    y=data['Heating_Bills'],
    mode='markers',
    marker=dict(size=10, color='royalblue'),
    name='Data'
)
fig.add_trace(scatter_data)

# Create an empty line plot for the regression line
line_data = go.Scatter3d(
    x=[],
    y=[],
    z=[],
    mode='lines',
    line=dict(color='red', width=3),
    name='Regression Line'
)
fig.add_trace(line_data)

# Create an empty scatter3d trace for the animated path
animated_path = go.Scatter3d(
    x=[],
    y=[],
    z=[],
    mode='lines',
    line=dict(color='lightgreen', width=2),
    name='Animated Path'
)
fig.add_trace(animated_path)

# Function to update the regression line and animated path
def update_line(num):
    line_data.x = data['Home_Size']
    line_data.y = data['Heating_Bills']
    line_data.z = regression_line(data['Home_Size'])
    
    animated_path.x = data['Home_Size'][:num+1]
    animated_path.y = data['Heating_Bills'][:num+1]
    animated_path.z = regression_line(data['Home_Size'][:num+1])
    
    fig.update_layout(title=f"Mathematical Dance: Step {num + 1}/{len(data)}")

# Animate the regression line
frames = [go.Frame(data=[go.Scatter3d(x=data['Home_Size'][:num+1], 
                                     y=data['Heating_Bills'][:num+1], 
                                     z=regression_line(data['Home_Size'][:num+1])),
                         go.Scatter3d(x=data['Home_Size'][:num+1], 
                                      y=data['Heating_Bills'][:num+1], 
                                      z=regression_line(data['Home_Size'][:num+1]))],
                   name=str(num)) for num in range(len(data))]

fig.update(frames=frames)
fig.update_layout(updatemenus=[dict(type='buttons', showactive=False,
                                    buttons=[dict(label='Play',
                                                  method='animate',
                                                  args=[None, 
                                                        dict(frame=dict(duration=200, 
                                                                        redraw=True), 
                                                             fromcurrent=True,
                                                             mode='immediate')]),
                                            dict(label='Pause',
                                                  method='animate',
                                                  args=[[None], 
                                                        dict(frame=dict(duration=0, 
                                                                        redraw=False), 
                                                             mode='immediate')])])])

fig.show()
