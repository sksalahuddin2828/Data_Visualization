import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import plotly.graph_objects as go
import sympy as sp

# Given tan(x)
tan_x = 5/12

# Calculate sec(x)
sec_x = np.sqrt(1 + tan_x**2)

# Function to calculate and visualize trigonometric functions
def plot_trigonometric_functions():
    x = np.linspace(0, 2*np.pi, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    y3 = np.tan(x)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x, y1, label='sin(x)')
    ax.plot(x, y2, label='cos(x)')
    ax.plot(x, y3, label='tan(x)')
    
    ax.legend()
    ax.set_title('Trigonometric Functions')
    ax.set_xlabel('x')
    ax.set_ylabel('Value')
    
    plt.show()

# Create an animated 3D surface plot using Plotly
def animate_3d_surface():
    x_values = np.linspace(0, 2*np.pi, 100)
    y_values = np.linspace(0, 2*np.pi, 100)
    X, Y = np.meshgrid(x_values, y_values)
    Z = np.sin(X) * np.cos(Y)

    fig = go.Figure(data=[go.Surface(z=Z, colorscale='Viridis')])
    frames = [go.Frame(data=[go.Surface(z=np.sin(X + i) * np.cos(Y + i))], name=str(i)) for i in np.arange(0, 2*np.pi, 0.1)]

    fig.update(frames=frames)
    fig.show()

# Display sec(x) value and additional mathematical calculations
def display_mathematical_calculations():
    # Additional calculations, expressions, and theories can be added here
    print(f"The value of sec(x) is: {sec_x}")

# Main function to run the project
def main():
    plot_trigonometric_functions()
    animate_3d_surface()
    display_mathematical_calculations()

if __name__ == "__main__":
    main()
