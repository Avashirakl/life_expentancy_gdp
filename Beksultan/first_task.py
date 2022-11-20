import pandas as pd

df = pd.read_csv('../all_data.csv')

df1 = df.groupby('Country').count()
df_pivot = pd.pivot_table(df, values='Life expectancy at birth (years)', index='Year', columns='Country')
df_pivot['Longest living country'] = df_pivot.idxmax(axis=1)
df_pivot.drop(df_pivot.loc[:, 'Chile':'Zimbabwe'], axis=1, inplace=True)
print(df_pivot)
