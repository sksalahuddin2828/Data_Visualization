from sklearn.linear_model import LinearRegression

# Using the synthetic data from Step 2 (x_values, y_values)
# Reshape the data for sklearn
X = x_values.reshape(-1, 1)
y = y_values

# Create and fit the linear regression model
model = LinearRegression()
model.fit(X, y)

# Get the coefficients of the linear regression line
slope = model.coef_[0]
intercept = model.intercept_

# Plot the synthetic data and the linear regression line
plt.scatter(X, y, label='Data')
plt.plot(X, model.predict(X), color='red', label='Linear Regression')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Regression Fit for y = 2x^2 + 3x + 1')
plt.legend()
plt.grid(True)
plt.show()
