import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('iris')

g = sns.PairGrid(df)

g.map_diag(plt.hist)

g.map_offdiag(plt.scatter)

plt.show()
