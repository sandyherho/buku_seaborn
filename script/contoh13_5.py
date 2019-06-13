import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('anscombe')

sns.lmplot(x='x', y='y', data=df.query("dataset == 'II'"), order=2)

plt.show()
