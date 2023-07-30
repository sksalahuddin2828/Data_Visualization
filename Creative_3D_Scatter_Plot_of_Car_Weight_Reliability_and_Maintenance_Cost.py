import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# Sample data (you can replace this with your actual data)
car_data = pd.DataFrame({
    'car_weight': [1500, 1800, 2000, 2200, 2400],
    'reliability': [0.9, 0.8, 0.7, 0.6, 0.5],
    'maintenance_cost': [1000, 1200, 1500, 1800, 2000]
})

# Create 3D scatter plot
fig = px.scatter_3d(car_data, x='car_weight', y='reliability', z='maintenance_cost',
                    color='car_weight', size='maintenance_cost', opacity=0.8,
                    title='3D Scatter Plot of Car Weight, Reliability, and Maintenance Cost',
                    labels={'car_weight': 'Car Weight', 'reliability': 'Reliability', 'maintenance_cost': 'Maintenance Cost'})

# Fit a regression plane to the data points
model_3d = np.polyfit(car_data['car_weight'], car_data['maintenance_cost'], 1)
plane_points = np.array([min(car_data['car_weight']), max(car_data['car_weight'])])
z_plane = np.polyval(model_3d, plane_points)
plane_trace = go.Scatter3d(x=plane_points, y=[0, 0], z=z_plane, mode='lines',
                           line=dict(color='black', width=3), showlegend=False)
fig.add_trace(plane_trace)

# Show the figure
fig.show()

# Print correlation coefficients
correlation_reliability = np.corrcoef(car_data['car_weight'], car_data['reliability'])[0, 1]
correlation_maintenance_cost = np.corrcoef(car_data['car_weight'], car_data['maintenance_cost'])[0, 1]
print("Correlation between car weight and reliability:", correlation_reliability)
print("Correlation between car weight and maintenance cost:", correlation_maintenance_cost)
