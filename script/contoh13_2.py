import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('tips')

sns.lmplot(x='size', y='tip', data=df)

plt.show()
