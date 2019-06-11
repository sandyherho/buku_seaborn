import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def plotsin(flip=1):
    x = np.linspace(0,14,100)
    for i in range(1,5):
        plt.plot(x,np.sin(x + i * 0.5) * (7 - i) * flip)

sns.set()

sns.set_style('white')

plotsin()

sns.despine()

plt.show()

