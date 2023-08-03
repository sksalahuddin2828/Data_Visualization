import matplotlib.pyplot as plt
from matplotlib_venn import venn2

# Create a Venn diagram for a + b = b + a
plt.figure(figsize=(6, 6))
venn2(subsets=(1, 1, 1), set_labels=('a + b', 'b + a'))
plt.title('Commutative Property: a + b = b + a')
plt.show()

# Create a Venn diagram for a * b = b * a
plt.figure(figsize=(6, 6))
venn2(subsets=(1, 1, 1), set_labels=('a * b', 'b * a'))
plt.title('Commutative Property: a * b = b * a')
plt.show()
