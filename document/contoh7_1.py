import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('iris')

sns.jointplot(x='petal_length', y='petal_width', data=df)

plt.show()
