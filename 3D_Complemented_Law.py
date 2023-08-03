import matplotlib.pyplot as plt
from matplotlib_venn import venn2

# Create a Venn diagram for a + a' = 1
plt.figure(figsize=(6, 6))
venn2(subsets=(1, 0, 0), set_labels=('a + a\'', '1'))
plt.title('Complemented Law: a + a\' = 1')
plt.show()

# Create a Venn diagram for a * a' = 0
plt.figure(figsize=(6, 6))
venn2(subsets=(0, 0, 1), set_labels=('a * a\'', '0'))
plt.title('Complemented Law: a * a\' = 0')
plt.show()
