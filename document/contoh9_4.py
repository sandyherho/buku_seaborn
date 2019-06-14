import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('iris')

sns.boxplot(x='species', y='petal_length', data=df)
plt.show()
