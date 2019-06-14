import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('tips')

g = sns.FacetGrid(df, col = "sex", hue = "smoker")

g.map(plt.scatter, "total_bill", "tip")

plt.show()
