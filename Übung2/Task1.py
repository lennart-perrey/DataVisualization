import numpy as np
import matplotlib.pyplot as plt

#Figure 1
np.random.seed(42)
num_points = 20
theta = np.linspace(0, 2*np.pi, num_points)
r = np.ones(num_points)
x = r * np.cos(theta)
y = r * np.sin(theta)
description = "Points with the law of proximity and symmetry, perceived as a complete circle"
plt.text(0.5, -0.1, description, horizontalalignment='center', verticalalignment='center', fontsize=10, transform=plt.gca().transAxes)
plt.scatter(x, y, s=30, c='black', alpha=0.7, edgecolors='none')
plt.gca().set_aspect('equal', adjustable='box')
plt.show()


#Figure 2
num_points = 30
theta = np.linspace(np.pi, 2*np.pi, num_points)
r = np.ones(num_points)
x = r * np.cos(theta)
y = r * np.sin(theta)
description = "Points with the law of symmetry and continuity, forming a 'U' shape"
plt.text(0.5, -0.1, description, horizontalalignment='center', verticalalignment='center', fontsize=10, transform=plt.gca().transAxes)
plt.scatter(x, y, s=30, c='black', alpha=0.7, edgecolors='none')
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

#Figure 3
np.random.seed(42)
num_points = 100
x = np.random.uniform(0, 1, num_points)
y = np.random.uniform(0, 1, num_points)
description = "Points of unequal distance, diffusely distributed, repelling each other, attracted to the edge"
plt.text(0.5, -0.1, description, horizontalalignment='center', verticalalignment='center', fontsize=10, transform=plt.gca().transAxes)
plt.scatter(x, y, s=30, c='black', alpha=0.7, edgecolors='none')
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

#Figure 3
np.random.seed(42)
num_points = 20 
theta = np.linspace(0, 2*np.pi, num_points)
r = np.linspace(0, 1, num_points)
x = r * np.cos(theta)
y = r * np.sin(theta)
description = "Collection of points contracting towards the center"
plt.text(0.5, -0.1, description, horizontalalignment='center', verticalalignment='center', fontsize=10, transform=plt.gca().transAxes)
plt.scatter(x, y, s=30, c='black', alpha=0.7, edgecolors='none')
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

#Figure 4
np.random.seed(42)
num_points = 20
theta = np.linspace(0, 2*np.pi, num_points)
r = np.ones(num_points)
sizes = np.random.uniform(10, 100, num_points)
x_large = 0
y_large = 0
x = r * np.cos(theta)
y = r * np.sin(theta)
description = "Points with the law of figure and ground, proximity, depicting a sun"
plt.text(0.5, -0.1, description, horizontalalignment='center', verticalalignment='center', fontsize=10, transform=plt.gca().transAxes)
plt.scatter(x_large, y_large, s=10000, c='black', alpha=0.7, edgecolors='none')  
plt.scatter(x, y, s=sizes, c='black', alpha=0.7, edgecolors='none')
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

#Figure 5
num_points = 20
theta = np.linspace(0, 2 * np.pi, num_points)
r = np.linspace(0, 1, num_points)
x = r * np.cos(theta)
y = r * np.sin(theta)
description = "Points with the appearance of high-speed motion, smashing, and massive"
plt.text(0.5, -0.1, description, horizontalalignment='center', verticalalignment='center', fontsize=10, transform=plt.gca().transAxes)
plt.scatter(x, y, s=np.linspace(1, 1000, num_points), c='black', alpha=0.7, edgecolors='none')
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

#Figure 6
np.random.seed(42)
num_points = 100
x = np.random.uniform(-1, 1, num_points)
y = np.random.uniform(-1, 1, num_points)
z = np.random.uniform(-1, 1, num_points)
sizes = np.random.uniform(10, 100, num_points)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, s=sizes, c='black', alpha=0.7, edgecolors='none')
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False
ax.grid(False)
ax.xaxis.line.set_lw(0)
ax.yaxis.line.set_lw(0)
ax.zaxis.line.set_lw(0)
plt.show()

#Figure 7
np.random.seed(42)
num_points = 100
x_large = np.random.uniform(0.75, 1, num_points)
y_large = np.random.uniform(0, 0.25, num_points)
sizes_large = np.random.uniform(30, 100, num_points)
x_medium = np.random.uniform(0.5, 0.75, num_points)
y_medium = np.random.uniform(0.25, 0.5, num_points)
sizes_medium = np.random.uniform(10, 30, num_points)
x_small = np.random.uniform(0.25, 0.5, num_points)
y_small = np.random.uniform(0.5, 0.75, num_points)
sizes_small = np.random.uniform(5, 10, num_points)
description = "Points moving from bottom right to top left, smaller points chasing larger points"
plt.text(0.5, -0.1, description, horizontalalignment='center', verticalalignment='center', fontsize=10, transform=plt.gca().transAxes)
plt.scatter(x_large, y_large, s=sizes_large, c='black', alpha=0.7, edgecolors='none')
plt.scatter(x_medium, y_medium, s=sizes_medium, c='black', alpha=0.7, edgecolors='none') 
plt.scatter(x_small, y_small, s=sizes_small, c='black', alpha=0.7, edgecolors='none') 
plt.show()
