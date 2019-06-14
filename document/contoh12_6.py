import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('iris')

g = sns.PairGrid(df)

g.map_upper(plt.scatter)

g.map_lower(sns.kdeplot, cmap='Blues_d')

g.map_diag(sns.kdeplot, lw=4, legend=False)

plt.show()
