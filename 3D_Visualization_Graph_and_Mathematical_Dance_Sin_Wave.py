import itertools
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import plotly.express as px

# Step 1: Dynamic Pizza Creation
sauces = ['Tomato', 'Pesto', 'Alfredo', 'BBQ']
breads = ['Thin Crust', 'Regular', 'Whole Wheat', 'Gluten-Free']
cheeses = ['Mozzarella', 'Cheddar', 'Parmesan']

pizza_combinations = list(itertools.product(sauces, breads, cheeses))
num_combinations = len(pizza_combinations)

# Step 2: Graph Theory Concepts
G = nx.Graph()
G.add_nodes_from(sauces, category='Sauce')
G.add_nodes_from(breads, category='Bread')
G.add_nodes_from(cheeses, category='Cheese')

for sauce, bread, cheese in pizza_combinations:
    G.add_edge(sauce, bread)
    G.add_edge(bread, cheese)

# Step 3: Data Visualization with Plotly
category_counts = {
    'Sauce': len(sauces),
    'Bread': len(breads),
    'Cheese': len(cheeses)
}

fig = px.bar(
    x=list(category_counts.keys()),
    y=list(category_counts.values()),
    title="Pizza Category Combinations"
)
fig.show()

# Step 4: Mathematical Dance and Expression (visualization using Matplotlib)
x = np.linspace(-2*np.pi, 2*np.pi, 1000)
y = np.sin(x)

plt.plot(x, y)
plt.title('Mathematical Dance: Sin Wave')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.grid(True)
plt.show()

# Step 5: Creative 3D Visualization (visualization using Matplotlib)
from mpl_toolkits.mplot3d import Axes3D

fig_3d = plt.figure()
ax = fig_3d.add_subplot(111, projection='3d')

x = np.random.rand(num_combinations)
y = np.random.rand(num_combinations)
z = np.random.rand(num_combinations)

ax.scatter(x, y, z)
ax.set_title('Creative 3D Visualization')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
