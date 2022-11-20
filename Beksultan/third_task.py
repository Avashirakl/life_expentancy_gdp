import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../all_data.csv')

df_2000_2005 = df.loc[(df['Year'] < 2005) & (df['Year'] >= 2000)]
df_2005_2010 = df.loc[(df['Year'] < 2010) & (df['Year'] >= 2005)]
df_2010_2015 = df.loc[(df['Year'] <= 2015) & (df['Year'] >= 2010)]


df2 = df_2000_2005.groupby('Country').mean()
df3 = df2.drop(['Year'], axis=1)
df3.reset_index(inplace=True)

df4 = df_2005_2010.groupby('Country').mean()
df5 = df4.drop(['Year'], axis=1)
df5.reset_index(inplace=True)

df6 = df_2010_2015.groupby('Country').mean()
df7 = df6.drop(['Year'], axis=1)
df7.reset_index(inplace=True)

df3.plot.bar(x="Country")
df5.plot.bar(x="Country")
df7.plot.bar(x="Country")

plt.show()