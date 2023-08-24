import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display
from matplotlib_venn import venn2

# Example sets
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Function to update Venn diagram
def update_venn(a_size, b_size):
    plt.clf()
    venn = venn2(subsets=(a_size, b_size, len(A & B)))
    plt.title(f"Venn Diagram\nA size: {a_size}, B size: {b_size}")
    plt.show()

# Create interactive slider widgets
a_slider = widgets.IntSlider(value=len(A), min=0, max=len(A) + 10, step=1, description='A Size:')
b_slider = widgets.IntSlider(value=len(B), min=0, max=len(B) + 10, step=1, description='B Size:')

# Create interactive output
out = widgets.interactive_output(update_venn, {'a_size': a_slider, 'b_size': b_slider})

# Display sliders and output
widgets.VBox([a_slider, b_slider, out])
