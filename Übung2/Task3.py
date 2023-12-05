'''
Left Plot:
Gestalt Laws: Proximity; Similarity
Effects: We can only perceive, that the plot contains two different datasets, that are being visualized, highlighted by dotted and cubed datapoints.
There is an orientation to the left side of the coordinate system.

Right Plot:
Gestalt Laws: Similarity; Enclosure; Connection
Effects: In this plot, the datasets are now conneced. This contributes to the fact, that we are now able to see
peaks and minima. We can also assume, that the plot is depicting a timframe. The enclosure from the dotted circle also highlights the local maxima
in both graphs and we are able to compare the datapoints.
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df1 = pd.DataFrame({'Time': np.arange(1, 11),
                    'Values': np.random.randint(10, 30, size=10)})

df2 = pd.DataFrame({'Time': np.arange(1, 11),
                    'Values': np.random.randint(5, 25, size=10)})

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))

axes[0].scatter(df1['Time'], df1['Values'], marker='o')
axes[0].scatter(df2['Time'], df2['Values'], marker='s')

axes[1].plot(df1['Time'], df1['Values'], marker='o')
axes[1].plot(df2['Time'], df2['Values'], marker='s')

peaks_df1 = df1[df1['Values'] == df1['Values'].max()]
peaks_df2 = df2[df2['Values'] == df2['Values'].max()]

circle_df1 = plt.Circle((peaks_df1['Time'].values[0], peaks_df1['Values'].values[0]),
                        1, fill=False, linestyle='dotted')

circle_df2 = plt.Circle((peaks_df2['Time'].values[0], peaks_df2['Values'].values[0]),
                        1,  fill=False, linestyle='dotted')

axes[1].add_patch(circle_df1)
axes[1].add_patch(circle_df2)

plt.show()
