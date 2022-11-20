import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('all_data.csv')

df.set_index('Year', inplace=True)
df.groupby('Country')['GDP'].plot(legend=True)

plt.title("GDP graph")
plt.xlabel("Year")
plt.ylabel("GDP")
plt.grid()
plt.show()
