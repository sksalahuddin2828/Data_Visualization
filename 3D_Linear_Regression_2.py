import matplotlib.animation as animation

def animate(i):
    line.set_ydata(model.predict(X) + 0.1 * i)
    return line,

fig, ax = plt.subplots()
ax.scatter(X, y, label='Data')
line, = ax.plot(X, model.predict(X), color='red', label='Linear Regression')

ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=True)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Animated Linear Regression Fit')
plt.grid(True)
plt.legend()

# Save the animation to a file (optional)
# ani.save('linear_regression_animation.gif', writer='pillow')

# Show the animation
plt.show()
