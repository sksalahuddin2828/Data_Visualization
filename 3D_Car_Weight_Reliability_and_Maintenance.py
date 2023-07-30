from mpl_toolkits.mplot3d import Axes3D

# Create 3D plot for car weight, reliability, and maintenance cost
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Extract data for the 3D plot
x = car_data['car_weight']
y = car_data['reliability']
z = car_data['maintenance_cost']

# Plot the data points
ax.scatter(x, y, z, c='red', marker='o', s=100)

# Set labels and title
ax.set_xlabel('Car Weight')
ax.set_ylabel('Reliability')
ax.set_zlabel('Maintenance Cost')
ax.set_title('3D Scatter Plot of Car Weight, Reliability, and Maintenance Cost')

# Show the 3D plot
plt.show()
