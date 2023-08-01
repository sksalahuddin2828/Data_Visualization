import matplotlib.pyplot as plt

# Create a scatter plot with Matplotlib
x = [1, 2, 3, 4, 5]
y = [10, 8, 6, 4, 2]

plt.scatter(x, y, label='Scatter Plot', color='red')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot Example')
plt.legend()
plt.show()
