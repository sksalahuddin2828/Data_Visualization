import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd

def pareto_principle(data):
    # Convert the dictionary data to a pandas DataFrame for easier manipulation
    df = pd.DataFrame(data)
    
    # Sort the data in descending order based on values
    sorted_data = df.sort_values(by='Value', ascending=False)

    # Calculate the cumulative sum of values
    cumulative_sum = sorted_data['Value'].cumsum()

    # Calculate the total value
    total_value = cumulative_sum.iloc[-1]

    # Find the threshold value that represents 80% of the total value
    threshold = total_value * 0.8

    # Find the index where the cumulative sum exceeds the threshold
    index_80 = np.argmax(cumulative_sum >= threshold)

    # Extract the top 20% of items based on the index
    top_20_items = sorted_data.iloc[:index_80 + 1]

    # Calculate the percentage of total value contributed by the top 20% items
    percentage_80 = (top_20_items['Value'].sum() / total_value) * 100

    return top_20_items, percentage_80

def create_random_data(num_items):
    # Generate random data for demonstration
    item_names = [f"Item{i}" for i in range(num_items)]
    values = np.random.randint(100, 1000, size=num_items)
    data = {"Item": item_names, "Value": values}
    return data

def visualize_data(data, percentage_80):
    # Create a 3D bar chart to visualize the data
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    items = data['Item']
    values = data['Value']

    xpos = np.arange(len(items))
    ypos = np.zeros(len(items))

    zpos = np.zeros(len(items))
    dx = dy = 0.5
    dz = values

    ax.bar3d(xpos, ypos, zpos, dx, dy, dz, shade=True)

    ax.set_xlabel('Items')
    ax.set_ylabel('Percentage of Total Value')
    ax.set_zlabel('Value')
    ax.set_title('Pareto Principle Visualization')

    # Add annotations to show the percentage of total value contributed by top 20% items
    annotation_text = f"Top 20% Items: {percentage_80:.2f}% of Total Value"
    ax.text2D(0.05, 0.95, annotation_text, transform=ax.transAxes)

    plt.show()

def main():
    # Generate random data with 100 items
    num_items = 100
    data = create_random_data(num_items)

    # Apply the Pareto Principle and get the top 20% items and their contribution percentage
    top_20_items, percentage_80 = pareto_principle(data)

    # Visualize the data using a creative 3D bar chart
    visualize_data(top_20_items, percentage_80)

if __name__ == '__main__':
    main()
