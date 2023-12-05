'''
Ordering the specified channels from lowest to highest effectiveness for encoding data:
Saturation -> Area -> Luminance -> Length -> Position, with position being considered one of the most effective channels for precise and intuitive quantitative comparisons.
'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = 'auto-mpg.csv' 
df = pd.read_csv(url)

plt.figure(figsize=(10, 6))
sns.scatterplot(x='acceleration', y='mpg', data=df, alpha=0.7, color='blue')
plt.title('Scatter Plot: mpg vs acceleration')
plt.xlabel('Acceleration')
plt.ylabel('Miles per Gallon')
plt.show()

plt.figure(figsize=(10, 6))
sns.jointplot(x='acceleration', y='mpg', data=df, kind='hex', cmap='viridis')
plt.suptitle('Hexbin Plot: mpg vs acceleration', y=1.02)
plt.show()

plt.figure(figsize=(10, 6))
sns.kdeplot(x='acceleration', y='mpg', data=df, fill=True, cmap='YlGnBu')
plt.title('2D KDE Plot: mpg vs acceleration')
plt.xlabel('Acceleration')
plt.ylabel('Miles per Gallon')
plt.show()

'''
Scatter Plot:
shows each data point with a dot, allowing to observe the relationship between acceleration and miles/gallon. Blue is chosen for better visibility.

Hexbin Plot: 
Dealing with a large number of data points. divides the space into hexagonal bins and colors them based on the number of points in each bin. Viridis colormap is chosen for its perceptually uniform colors.

2D KDE Plot: 
provides a smooth representation of the distribution. color in this plot represents the density of points. colormap is chosen for its sequential color progression.
'''