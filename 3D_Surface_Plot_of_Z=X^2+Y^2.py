import torch

x = torch.tensor(2.0, requires_grad=True)
y = x**2 + 3*x + 1

y.backward()
gradient = x.grad
print("Expression:", y)
print("Gradient:", gradient)

from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title('Surface Plot of Z = X^2 + Y^2')
plt.show()
