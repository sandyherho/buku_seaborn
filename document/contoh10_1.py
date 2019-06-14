import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('titanic')

sns.barplot(x='sex', y='survived', hue='class', data=df)

plt.show()
