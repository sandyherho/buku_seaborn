import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('tips')

sns.regplot(x='total_bill', y='tip', data=df)

sns.lmplot(x='total_bill', y='tip', data=df)

plt.show()
