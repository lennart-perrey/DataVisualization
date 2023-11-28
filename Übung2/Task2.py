'''
Weber's Law and Fechner's Law are both principles in the field of psychophysics, which is the study of the relationship between physical stimuli and the sensations they produce.
While Weber's Law focuses on the relative differences between stimuli, Fechner's Law addresses the relationship between the intensity of a physical stimulus and the perceived sensation, incorporating a logarithmic scaling to capture the non-linear nature of perception.

Weber's Law:
Weber's Law states that the just noticeable difference between two stimuli is proportional to the magnitude of the stimuli. In other words, the ability to perceive a difference between two stimuli depends on the ratio of the difference to the initial stimulus.
Weber's Law suggests that our sensitivity to differences in stimuli is relative, and the just noticeable difference is a constant ratio rather than a constant difference. This law is often applied in areas such as marketing, where companies adjust the intensity of stimuli to meet the threshold of perceptible differences.

Fechner's Law:
Fechner's Law describes the relationship between the intensity of a physical stimulus and the perceived intensity of the corresponding sensation. It states that the perceived sensation is proportional to the logarithm of the stimulus intensity.
The logarithmic function in Fechner's Law reflects the idea that our perception of stimulus intensity is not linear but logarithmic. This means that as the physical stimulus increases geometrically, the perceived sensation increases arithmetically. The logarithmic scaling accounts for the diminishing returns in perceived sensation as the stimulus becomes more intense.

'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from random import sample

def generate_data(num_points):
    df = pd.DataFrame(np.random.random_sample(size=(num_points, 2)), columns=list('xy'))
    return df

def plot_points(df, title):
    plt.scatter(df['x'], df['y'])
    plt.title(title)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()

def spot_the_difference(df1, df2):
    return not df1.equals(df2)

def main():

    df1 = generate_data(10)
    df2 = generate_data(110)
    df3 = generate_data(20)
    df4 = generate_data(120)

    different_points = sample(range(0, 10), 2)
    df2.iloc[different_points] = np.random.random_sample(size=(2, 2))

    different_points = sample(range(0, 20), 3)
    df3.iloc[different_points] = np.random.random_sample(size=(3, 2))

    different_points = sample(range(0, 120), 4)
    df4.iloc[different_points] = np.random.random_sample(size=(4, 2))
    plot_points(df1, 'Visualization 1 (10 points)')
    plot_points(df2, 'Visualization 2 (110 points) - Spot the Difference!')
    plot_points(df3, 'Visualization 3 (20 points) - Spot the Difference!')
    plot_points(df4, 'Visualization 4 (120 points) - Spot the Difference!')
    print("Can you spot the differences?")


if __name__ == "__main__":
    main()
