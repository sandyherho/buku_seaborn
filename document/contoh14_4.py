import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('flights')

df = df.pivot_table(index='month', columns='year', values='passengers')

print(df)

sns.heatmap(df, cmap='seismic', linecolor='black', lw=1)

plt.show()
