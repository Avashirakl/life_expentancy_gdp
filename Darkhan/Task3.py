from tabulate import tabulate
import pandas as pd
import numpy as np

df_main = pd.read_csv('changed.csv')

df1 = df_main[df_main.groupby(['Country', 'Year'])['GDP'].transform(max) == df_main['GDP']].sort_values(['Year', 'GDP'], ascending=True)

columns = {'The richest country in the year': [], 'Year': [], 'GDP': []}
index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
res = pd.DataFrame(data={}, columns=columns, index=index)  # new dataframe

x = 1
for i in range(5, 96, 6):  # inserting data to new dataframe
    res.at[x, 'The richest country in the year'] = df1.iloc[i]['Country']
    res.at[x, 'Year'] = df1.iloc[i]['Year']
    res.at[x, 'GDP'] = df1.iloc[i]['GDP']
    x += 1

df2 = pd.DataFrame(df1)

del df2["Unnamed: 0"]  # deleted unnecessary column
df2 = df2.reset_index(drop=True)  # reset index
df2.index = np.arange(1, len(df2) + 1)  # make index start from 1
df2.index.name = None

print()
print()
print('Table of countries sorted by columns \'Year\' and \'GDP\' to show the richest country every year')
print(tabulate(df2, headers='keys', tablefmt='psql'))
print()
print()
print()
print('Table of the richest country every year')
print(tabulate(res, headers='keys', tablefmt='psql'))