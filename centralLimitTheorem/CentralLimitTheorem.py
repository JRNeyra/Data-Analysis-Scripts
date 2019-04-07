#########################################################
# Description: This script implements the Central Limit
# Theorem model and tests its result as more samples
# are added to the calculations.
# Author: Jose Neyra
#########################################################

import numpy as np
import matplotlib.pyplot as plt

nrows = 3
ncols = 3
f, axarr = plt.subplots(nrows=nrows, ncols=ncols, sharex=True)

nRandomVariables = -3
increment = 4
n = 10 ** 6

for row in range(nrows):
    for col in range(ncols):
        nRandomVariables = nRandomVariables + increment
        X = np.random.rand(nRandomVariables, n)
        S = np.mean(X, axis=0)
        hist, bEdges = np.histogram(S, bins=1000)
        bCenters = np.array([0.5 * (bEdges[i] + bEdges[i + 1]) for i in range(len(bEdges) - 1)])
        axarr[row][col].stem(bCenters, hist)
        axarr[row][col].set_title('N=%d' % nRandomVariables)
plt.show()
