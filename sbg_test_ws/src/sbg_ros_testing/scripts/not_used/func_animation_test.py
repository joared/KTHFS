#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x = []
y = []
i = 0

def animate(i):
    i += 1
    x.append(i)
    y.append(np.random.random()*10)
    plt.cla()
    plt.plot(x, y)

if __name__ == "__main__":
    fig = plt.figure()
    ani = FuncAnimation(fig, animate, interval=1)
    #plt.tight_layout()
    plt.show()