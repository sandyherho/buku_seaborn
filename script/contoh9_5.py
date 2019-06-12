import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('tips')

sns.violinplot(x='day', y='total_bill', data=df)

plt.show()
