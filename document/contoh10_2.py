import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('titanic')

sns.countplot(x='class', data=df, palette='Reds')

plt.show()
