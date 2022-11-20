import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('all_data.csv')


df.set_index('Year', inplace=True)
df.groupby('Country')['Life expectancy at birth (years)'].plot(legend=True)

plt.title("Life expectancy at birth and year graph")
plt.xlabel("Year")
plt.ylabel("Life expectancy at birth (years)")
plt.grid()
plt.show()






