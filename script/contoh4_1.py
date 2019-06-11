import numpy as np
import matplotlib.pyplot as plt

def plotsin(flip=1):
    x = np.linspace(0,14,100)
    for i in range(1,5):
        plt.plot(x, np.sin(x + i*0.5)*(7 - i) * flip)

plotsin()

plt.show()
