import matplotlib.pyplot as plt
import numpy as np

# Define the operation table for Example 1
operation_table = np.array([[0, 1, 2],
                            [1, 0, 2],
                            [2, 2, 0]])

# Check for inverse property
def has_inverse(x, y):
    for i in range(len(operation_table)):
        if operation_table[x][i] == y and operation_table[y][i] == x:
            return True
    return False

# Visualize the operation table
def visualize_operation_table():
    fig, ax = plt.subplots()
    cax = ax.matshow(operation_table, cmap='viridis')
    plt.xticks(np.arange(len(operation_table)), ['a', 'b', 'c'])
    plt.yticks(np.arange(len(operation_table)), ['a', 'b', 'c'])
    plt.xlabel('Element')
    plt.ylabel('Element')
    plt.title('Operation Table')
    plt.colorbar(cax)
    plt.show()

# Visualize the inverses
def visualize_inverses():
    plt.figure(figsize=(8, 6))
    x_vals = [0, 1, 2]  # Corresponding to ['a', 'b', 'c']
    y_vals = []
    for x in x_vals:
        inverse = None
        for y in x_vals:
            if has_inverse(x, y):
                inverse = y
                break
        y_vals.append(inverse)

    plt.scatter(x_vals, y_vals, color='blue', label='Inverses')
    plt.plot(x_vals, x_vals, color='red', linestyle='dashed', label='Identity')
    plt.xlabel('Element')
    plt.ylabel('Inverse')
    plt.title('Inverses in Example 1')
    plt.legend()
    plt.xticks(x_vals, ['a', 'b', 'c'])
    plt.show()

# Call the visualization functions
visualize_operation_table()
visualize_inverses()
