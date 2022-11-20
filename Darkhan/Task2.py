from tabulate import tabulate
import pandas as pd

df_main = pd.read_csv('changed.csv')
df1 = df_main.groupby('Country')['Life expectancy at birth (years)'].mean()  # group by 'Country' and find average of 'Life expectancy at birth (years)'
df2 = df_main.groupby('Country')['GDP'].mean()  # group by 'Country' and find average of 'GDP'

frames = [df1, df2]  # create list

result = pd.concat(frames, axis=1, join='outer')  # convert elements of list to dataframe by concatenating them
result.columns = ['Average life expectancy at birth', 'Average GDP']  # change column names

print()
print()
print()
print('+-------|Table of average of life expectancy at birth and GDP grouped by country|-------+')
print(tabulate(result, headers='keys', tablefmt='psql'))
