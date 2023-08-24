import matplotlib.pyplot as plt
from matplotlib_venn import venn2
import numpy as np

# Example sets
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Create Venn diagram
venn = venn2([A, B], ('A', 'B'))

# Set labels and titles
venn.get_label_by_id('10').set_text('A - B')
venn.get_label_by_id('01').set_text('B - A')
venn.get_label_by_id('11').set_text('A ∩ B')

plt.title('Venn Diagram of A and B')

# Display the plot
plt.show()
