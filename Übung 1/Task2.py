#!/usr/bin/python
import matplotlib.pyplot as plt
import pandas as pd

#1
file_path = "C:/Users/l.perrey.INTERN/Desktop/Übungen/Data Visualization/Übung 1/DatasaurusDozen.tsv"
file = pd.read_csv(file_path, sep='\t')

#2
statistics = file.describe()
print(statistics)

#3
datasets = file['dataset'].unique()

for dataset_name in datasets:
    subset = file[file['dataset'] == dataset_name]
    plt.scatter(subset['x'], subset['y'], label=dataset_name)
    
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.title('Datasaurus Dozen Datasets')
plt.show()