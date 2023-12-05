import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import brewer2mpl

file_path = "opendata_sh_abiturduchschnittsnoten_allg_bildend_2011-21.csv" 
df = pd.read_csv(file_path, sep=';',encoding='mbcs', nrows=12)
columns_of_interest = ['Jahr', 'Durchschnitt', 'Note 1.0', 'Note 1.1', 'Note 1.2', 'Note 1.3', 'Note 1.4',
                        'Note 1.5', 'Note 1.6', 'Note 1.7', 'Note 1.8', 'Note 1.9', 'Note 2.0', 'Note 2.1',
                        'Note 2.2', 'Note 2.3', 'Note 2.4', 'Note 2.5', 'Note 2.6', 'Note 2.7', 'Note 2.8',
                        'Note 2.9', 'Note 3.0', 'Note 3.1', 'Note 3.2', 'Note 3.3', 'Note 3.4', 'Note 3.5',
                        'Note 3.6', 'Note 3.7', 'Note 3.8', 'Note 3.9', 'Note 4.0', 'Nicht bestanden']

df = df[columns_of_interest]

df.plot(kind='bar', x='Jahr', y=df.columns[2:], stacked=True, title='default')
plt.show()

color_palette = brewer2mpl.get_map('Set3', 'qualitative', 12).mpl_colors
df.plot(kind='bar', x='Jahr', y=df.columns[2:], stacked=True, colormap=plt.cm.colors.ListedColormap(color_palette),
        title='color brewer')
plt.show()

df_aggregated = df.groupby('Jahr', axis=0).sum().iloc[:, ::2]
df_aggregated.plot(kind='bar', stacked=True, title='aggregated with a factor of 2')
plt.show()

grades_to_reduce = ['Note 1.0', 'Note 2.0', 'Note 3.0', 'Note 4.0', 'Nicht bestanden']
df_reduced_bins = df[['Jahr'] + grades_to_reduce]
df_reduced_bins = df_reduced_bins.groupby('Jahr', axis=0).sum()

df_reduced_bins.plot(kind='bar', stacked=True, title='reduced to 5 bins')
plt.show()