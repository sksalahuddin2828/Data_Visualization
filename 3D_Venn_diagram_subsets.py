import matplotlib.pyplot as plt
from matplotlib_venn import venn2

# Create a Venn diagram for a + (b * c) = (a + b) * (a + c)
plt.figure(figsize=(6, 6))
venn2(subsets=(1, 1, 1), set_labels=('a', '(b * c)'))
plt.text(0.55, 0.85, 'a', fontsize=15, color='black')
plt.text(0.35, 0.45, 'b * c', fontsize=15, color='black')
plt.text(0.15, 0.85, 'a + b', fontsize=15, color='black')
plt.text(0.35, 0.15, 'a + c', fontsize=15, color='black')
plt.title('Distributive Property: a + (b * c) = (a + b) * (a + c)')
plt.show()

# Create a Venn diagram for a * (b + c) = (a * b) + (a * c)
plt.figure(figsize=(6, 6))
venn2(subsets=(1, 1, 1), set_labels=('a', '(b + c)'))
plt.text(0.55, 0.85, 'a', fontsize=15, color='black')
plt.text(0.35, 0.45, 'b + c', fontsize=15, color='black')
plt.text(0.15, 0.85, 'a * b', fontsize=15, color='black')
plt.text(0.35, 0.15, 'a * c', fontsize=15, color='black')
plt.title('Distributive Property: a * (b + c) = (a * b) + (a * c)')
plt.show()
