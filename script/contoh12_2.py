import pandas as pd
import  matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('tips')

g = sns.FacetGrid(df, col = "time")

g.map(plt.hist, "tip")

plt.show()
