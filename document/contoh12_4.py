import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('iris')

g = sns.PairGrid(df)

g.map(plt.scatter)

plt.show()
