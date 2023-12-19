import matplotlib.pyplot as plt

sizes = [48.37, 51.63]  
colors = ['Green', 'Grey']
labels = ['Yes', '']


fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, colors=colors,  startangle=90)

centre_circle = plt.Circle((0, 0), 0.60, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.title('Most people in Hamburg supported the Olympic games in Hamburg')
plt.tight_layout()
plt.show()
