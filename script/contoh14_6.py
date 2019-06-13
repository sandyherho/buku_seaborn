import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('flights').pivot_table(index='month', columns='year', values='passengers')

sns.clustermap(df, cmap='coolwarm', standard_scale=1)

plt.show()
