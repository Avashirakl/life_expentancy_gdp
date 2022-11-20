import pandas as pd

df = pd.read_csv('../all_data.csv')

df_pivot1 = pd.pivot_table(df, values='Life expectancy at birth (years)', index='Country', columns='Year')
df_pivot1.drop(df_pivot1.loc[:, '2001':'2014'], axis=1, inplace=True)

df_pivot2 = pd.pivot_table(df, values='GDP', index='Country', columns='Year')
df_pivot2.drop(df_pivot2.loc[:, '2001':'2014'], axis=1, inplace=True)

all_data = pd.merge(df_pivot1, df_pivot2, left_index=True, right_index=True)
renamed = all_data.rename(columns={'2000_x': '2000_life', '2015_x': '2015_life', '2000_y': '2000_GDP', '2015_y': '2015_GDP'})
print(renamed)
