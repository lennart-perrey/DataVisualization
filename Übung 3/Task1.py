import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

values = [35, 75]

plt.subplot(4, 5, 1)
plt.scatter([1, 2], values)
plt.title("Scatter Plot")

plt.subplot(4, 5, 2)
plt.bar([1, 2], values)
plt.title("Bar Plot")

plt.subplot(4, 5, 3)
plt.plot([1, 2], values)
plt.title("Line Plot")

plt.subplot(4, 5, 4)
plt.barh([1, 2], values)
plt.title("Horizontal Bar Plot")

plt.subplot(4, 5, 5)
plt.pie(values, labels=["35", "75"], autopct="%1.1f%%")
plt.title("Pie Chart")

plt.subplot(4, 5, 6)
plt.boxplot([values])
plt.title("Box Plot")

plt.subplot(4, 5, 7)
plt.violinplot([values])
plt.title("Violin Plot")

plt.subplot(4, 5, 8)
plt.fill_between([1, 2], values, color="skyblue", alpha=0.4)
plt.title("Area Plot")

plt.subplot(4, 5, 9)
plt.hist(values)
plt.title("Histogram")

plt.subplot(4, 5, 10)
plt.hexbin([1, 2, 2, 1], [35, 35, 75, 75], gridsize=10, cmap='Blues')
plt.title("Hexbin Plot")

plt.subplot(4, 5, 11)
plt.stem([1, 2], values, basefmt='b')
plt.title("Stem Plot")

plt.subplot(4, 5, 12)
plt.errorbar([1, 2], values, yerr=[5, 10], fmt='o', capsize=5)
plt.title("Error Bar Plot")

plt.subplot(4, 5, 13, polar=True)
plt.plot([0, 1], [0, values[0]], marker='o')
plt.plot([0, 2], [0, values[1]], marker='o')
plt.title("Polar Plot")

ax = plt.subplot(4, 5, 14, projection='3d')
ax.bar([1, 2], values, zs=0, zdir='y', alpha=0.8)
plt.title("3D Bar Plot")


#TODO: Add more

plt.tight_layout()
plt.show()
