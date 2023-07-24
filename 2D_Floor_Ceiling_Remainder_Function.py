import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def floor_function(x):
    return np.floor(x)

def ceiling_function(x):
    return np.ceil(x)

def remainder_function(a, m):
    return np.mod(a, m)

def visualize_function(x, y, z, function_name):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    ax.scatter(x, y, z, s=400, marker='o', label=function_name)
    
    ax.set_xlabel('Input')
    ax.set_ylabel('Output')
    ax.set_zlabel('Value')
    
    plt.title(f"{function_name} Function Visualization")
    plt.legend()
    plt.show()

# Example 1 - Floor Function
x1 = np.array([3.5, -2.4, 3.143])
y1 = floor_function(x1)
visualize_function(x1, y1, y1, "Floor")

# Example 2 - Ceiling Function
x2 = np.array([3.5, -2.4, 3.143])
y2 = ceiling_function(x2)
visualize_function(x2, y2, y2, "Ceiling")

# Example 3 - Remainder Function
a = np.array([35, 20, 4])
m = np.array([7, 3, 9])
y3 = remainder_function(a, m)
visualize_function(a, m, y3, "Remainder")

print("Floor Function Values:", y1)
print("Ceiling Function Values:", y2)
print("Remainder Function Values:", y3)
