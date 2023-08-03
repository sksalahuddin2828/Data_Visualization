import matplotlib.pyplot as plt
from matplotlib_venn import venn2

# Create a Venn diagram for a + 0 = a
plt.figure(figsize=(6, 6))
venn2(subsets=(1, 0, 1), set_labels=('a + 0', 'a'))
plt.title('Identity Property: a + 0 = a')
plt.show()

# Create a Venn diagram for a * 1 = a
plt.figure(figsize=(6, 6))
venn2(subsets=(1, 0, 1), set_labels=('a * 1', 'a'))
plt.title('Identity Property: a * 1 = a')
plt.show()
