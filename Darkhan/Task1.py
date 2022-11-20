import pandas as pd

df_main = pd.read_csv('../all_data.csv')

list_of_gdp = []  # create list for saving 'GDP' values
for i in range(96):
    list_of_gdp.append(df_main['GDP'].iloc[i])  # save value of 'GDP' in every row to the list

df_main = df_main.assign(GDP=lambda x: x.GDP / 1000000000)  # divide it by 1 billion with lambda function for convenience working with data

df_main.to_csv('changed.csv')  # export to new csv file
