import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('iris')

sns.set_style('ticks')

sns.pairplot(df, hue='species', diag_kind='kde', kind='scatter', palette='husl')

plt.show()

