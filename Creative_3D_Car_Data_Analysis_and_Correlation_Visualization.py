import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from scipy import stats
import warnings

# Suppress the warning
warnings.filterwarnings("ignore", message="X does not have valid feature names")

# Sample data (you can replace this with your actual data)
car_data = pd.DataFrame({
    'car_weight': [1500, 1800, 2000, 2200, 2400],
    'reliability': [0.9, 0.8, 0.7, 0.6, 0.5],
    'maintenance_cost': [1000, 1200, 1500, 1800, 2000]
})

# Calculate correlation coefficients
correlation_reliability = np.corrcoef(car_data['car_weight'], car_data['reliability'])[0, 1]
correlation_maintenance_cost = np.corrcoef(car_data['car_weight'], car_data['maintenance_cost'])[0, 1]

# Fit regression lines
model_reliability = LinearRegression()
model_maintenance_cost = LinearRegression()
model_reliability.fit(car_data[['car_weight']], car_data['reliability'])
model_maintenance_cost.fit(car_data[['car_weight']], car_data['maintenance_cost'])

# Polynomial regression for maintenance cost
poly_features = PolynomialFeatures(degree=2)
X_poly = poly_features.fit_transform(car_data[['car_weight']])
model_maintenance_cost_poly = LinearRegression()
model_maintenance_cost_poly.fit(X_poly, car_data['maintenance_cost'])

# Print correlation coefficients
print("Correlation between car weight and reliability:", correlation_reliability)
print("Correlation between car weight and maintenance cost:", correlation_maintenance_cost)

# Calculate p-values for correlations
p_value_reliability = stats.pearsonr(car_data['car_weight'], car_data['reliability'])[1]
p_value_maintenance_cost = stats.pearsonr(car_data['car_weight'], car_data['maintenance_cost'])[1]

# Visualize the data and correlations using seaborn
sns.set(style='whitegrid', font_scale=1.2)

# Scatter plot for car weight and reliability with regression line
plt.figure(figsize=(8, 6))
sns.scatterplot(data=car_data, x='car_weight', y='reliability', s=100, color='blue')
plt.plot(car_data['car_weight'], model_reliability.predict(car_data[['car_weight']]), color='red', linewidth=2)
plt.xlabel('Car Weight')
plt.ylabel('Reliability')
plt.title('Scatter plot of Car Weight vs. Reliability with Regression Line')
plt.show()

# Scatter plot for car weight and maintenance cost with regression line
plt.figure(figsize=(8, 6))
sns.scatterplot(data=car_data, x='car_weight', y='maintenance_cost', s=100, color='green')
plt.plot(car_data['car_weight'], model_maintenance_cost.predict(car_data[['car_weight']]), color='red', linewidth=2)
plt.xlabel('Car Weight')
plt.ylabel('Maintenance Cost')
plt.title('Scatter plot of Car Weight vs. Maintenance Cost with Regression Line')
plt.show()

# 3D Scatter plot with regression plane for car weight, reliability, and maintenance cost using Plotly
fig = px.scatter_3d(car_data, x='car_weight', y='reliability', z='maintenance_cost',
                    color='car_weight', size='maintenance_cost', opacity=0.8,
                    title='3D Scatter Plot of Car Weight, Reliability, and Maintenance Cost',
                    labels={'car_weight': 'Car Weight', 'reliability': 'Reliability', 'maintenance_cost': 'Maintenance Cost'})

# Fit a plane to the data points
model_3d = LinearRegression()
model_3d.fit(car_data[['car_weight', 'reliability']], car_data['maintenance_cost'])

# Generate points for the plane
xx, yy = np.meshgrid(np.linspace(min(car_data['car_weight']), max(car_data['car_weight']), 10),
                     np.linspace(min(car_data['reliability']), max(car_data['reliability']), 10))
zz = model_3d.predict(np.array([xx.ravel(), yy.ravel()]).T).reshape(xx.shape)

# Plot the regression plane using Plotly's surface plot
fig.add_trace(go.Surface(x=xx, y=yy, z=zz, opacity=0.7, colorscale='Viridis'))

# Show the 3D plot using Plotly
fig.show()

# Print correlation p-values
print("P-value for correlation between car weight and reliability:", p_value_reliability)
print("P-value for correlation between car weight and maintenance cost:", p_value_maintenance_cost)
