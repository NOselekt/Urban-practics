import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)

matplotlib.rcParams['font.family'] = 'Times New Roman'
matplotlib.rcParams['font.size'] = 20

y = [[0.513, 0.193, -0.238, -0.528, -0.558, -0.328, 0.113, 0.483],
     [0.553, 0.283, -0.178, -0.498, -0.528, -0.298, 0.203, 0.623],
     [0.743, 0.273, -0.318, -0.628, -0.678, -0.418, 0.593, 0.703],
     [1.193, 0.343, -0.428, -0.818, -0.858, -0.598, 0.043, 1.043]]

x = [1, 2, 3, 4, 5, 6, 7, 8]
fig, ax = plt.subplots()
ax.plot(x, y[0], label='R=8')
ax.plot(x, y[1], label='R=6')
ax.plot(x, y[2], label='R=3')
ax.plot(x, y[3], label='R=0')
ax.scatter(x, y[0])
ax.scatter(x, y[1])
ax.scatter(x, y[2])
ax.scatter(x, y[3])
ax.grid(which='minor')
ax.grid(which='major')
ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator())
ax.set_xlabel('I, A')
ax.set_ylabel('B, мТл')
ax.legend()
plt.show()
