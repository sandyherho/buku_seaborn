import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('tips').corr()

sns.heatmap(df, annot=True, cmap='coolwarm')

plt.show()
