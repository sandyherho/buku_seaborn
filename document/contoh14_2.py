import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('tips')

df = df.corr()

print(df)

sns.heatmap(df)

plt.show()
