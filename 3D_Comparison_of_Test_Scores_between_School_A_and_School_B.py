import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Data for school A
mean_A = 1000
std_dev_A = 100
sample_size_A = 15

# Data for school B
mean_B = 950
std_dev_B = 90
sample_size_B = 20

# Confidence level
confidence_level = 0.90

# Calculate standard error
se = np.sqrt((std_dev_A ** 2) / sample_size_A + (std_dev_B ** 2) / sample_size_B)

# Calculate degrees of freedom
df = sample_size_A + sample_size_B - 2

# Calculate t critical value
t_critical = stats.t.ppf((1 + confidence_level) / 2, df)

# Calculate margin of error
margin_of_error = t_critical * se

# Calculate the difference in means
mean_difference = mean_A - mean_B

# Calculate the lower and upper bounds of the confidence interval
lower_bound = mean_difference - margin_of_error
upper_bound = mean_difference + margin_of_error

print(f"The 90% confidence interval for the difference in test scores is: ({lower_bound:.2f}, {upper_bound:.2f})")

# Create a pandas DataFrame to store the data
data = {
    'School': ['A', 'B'],
    'Mean': [mean_A, mean_B],
    'Sample Size': [sample_size_A, sample_size_B]
}
df = pd.DataFrame(data)

# Create a bar plot to compare means
fig, ax = plt.subplots()
ax.bar(df['School'], df['Mean'], yerr=[1.96 * (std_dev_A / np.sqrt(sample_size_A)), 1.96 * (std_dev_B / np.sqrt(sample_size_B))], capsize=5)
ax.set_ylabel('Mean Test Score')
ax.set_title('Comparison of Test Scores between School A and School B')
plt.show()
