#1
'''
UNEMP:
Meaning: The total number of unemployed individuals during a specified time period.
Data Type: Quantitative, interval
WAGES:
Meaning: The average wages earned per week by individuals.
Data Type: Quantitative, interval
BENEFITS:
Meaning: The amount of unemployment benefits that an individual is entitled to receive per week.
Data Type: Quantitative, interval.
BWRATIO:
Meaning: The proportion of weekly benefits relative to weekly wages.
Data Type: QUantitative, ratio.
NNP:
Meaning: The net value of goods and services produced by a country within a given time period, accounting for depreciation.
Data Type: Quantitative, interval.
DEMAND:
Meaning: The ratio of Net National Product to its trend value, indicating whether the current production is above or below the trend.
Data Type: Quantitative, ratio.
YEAR
Meaning: The time period or calendar year to which the data corresponds.
Data Type: Quantitative, temporal
'''
#2:
import pandas as pd
import matplotlib.pyplot as plt
file_path = "C:/Users/l.perrey.INTERN/Desktop/Übungen/Data Visualization/Übung 1/1669_BK.xlsx"
df = pd.read_excel(file_path)
df = df.rename(columns=lambda x: x.replace(',', '') if isinstance(x, str) else x)
print(df.head())

#3
# Heatmap for Correlation Matrix
import seaborn as sns
correlation_matrix = df[['UNEMP', 'WAGES', 'BENEFITS', 'BWRATIO', 'NNP', 'DEMAND']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap: Unemployment Factors')
plt.show()

# Bar Plot for Average Unemployment, Wages, and Benefits over the years
df_avg = df.groupby('YEAR').mean()
df_avg[['UNEMP', 'WAGES', 'BENEFITS']].plot(kind='bar', stacked=True)
plt.xlabel('Year')
plt.ylabel('Average Value')
plt.title('Average Unemployment, Wages, and Benefits over the Years')
plt.show()

#4
plt.plot(df['YEAR'], df['UNEMP'], marker='o')
plt.xlabel('Year')
plt.ylabel('Unemployment Level')
plt.title('Temporal Changes in Unemployment (Inter-war Britain)')
plt.show()

#5
plt.scatter(df['BENEFITS'], df['UNEMP'])
plt.xlabel('Benefits')
plt.ylabel('Unemployment Level')
plt.title('Correlation Between Benefits and Unemployment')
plt.show()
correlation_coefficient = df['BWRATIO'].corr(df['UNEMP'])
print(f'Correlation Coefficient: {correlation_coefficient}')
#Correlation Coefficient: 0.3867839839590683
#positive orrelation; Benjamin and Kochin’s hypothesis approved; correlation is not very high though;
#6
'''
Used Action: Analyze -> Consume -> Discover
Target: Attributes (many) -> Correlation 
We wanted to analyze the dataset, to see if theres a correlation between benefits with respect to unemployment.
'''
#7
#8
#9
df_no_1920 = df[df['YEAR'] != 1920]

plt.plot(df_no_1920['YEAR'], df_no_1920['UNEMP'], marker='o')
plt.xlabel('Year')
plt.ylabel('Unemployment Level')
plt.title('Temporal Changes in Unemployment (Inter-war Britain)')
plt.show()

plt.scatter(df_no_1920['BENEFITS'], df_no_1920['UNEMP'])
plt.xlabel('Benefits')
plt.ylabel('Unemployment Level')
plt.title('Correlation Between Benefits and Unemployment')
plt.show()
correlation_coefficient = df_no_1920['BWRATIO'].corr(df_no_1920['UNEMP'])
print(f'Correlation Coefficient: {correlation_coefficient}')