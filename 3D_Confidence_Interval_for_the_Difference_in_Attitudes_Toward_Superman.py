import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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

# Plot the 3D scatter plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(data["Boys"], data["Girls"], data["Difference"], c='b', marker='o')

# Set labels and title
ax.set_xlabel('Boys')
ax.set_ylabel('Girls')
ax.set_zlabel('Difference')
plt.title('Confidence Interval for the Difference in Attitudes Toward Superman')

# Add confidence interval lines
ax.plot([n_boys], [n_girls], [lower_bound], 'r', marker='o', markersize=8)
ax.plot([n_boys], [n_girls], [upper_bound], 'r', marker='o', markersize=8)

plt.show()
