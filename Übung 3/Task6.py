'''
Affected deficiency: Red-Blind/Protanopia
'''


import matplotlib.pyplot as plt

# Data
countries = ['USA', 'Australia']
green_values = [3.8, 1.3]  # in thousands of dollars
yellow_values = [7.2, 0.6]  # in thousands of dollars

# Bar chart
bar_width = 0.35
index = range(len(countries))

fig, ax = plt.subplots()
bar1 = ax.bar(index, green_values, bar_width,  color='green', hatch='//')
bar2 = ax.bar([i + bar_width for i in index], yellow_values, bar_width,  color='red', hatch='\\')

# Add labels, title, and legend
ax.set_xticks([i + bar_width / 2 for i in index])
ax.set_xticklabels(countries)
ax.legend()

# Display the plot
plt.show()