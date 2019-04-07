#########################################################
# Description: This script generates a random
# probabilities file that is then used in
# HuffmanCodingSimulation.py to create a Huffman code
# from its probabilities
# Author: Jose Neyra
#########################################################


import numpy as np

N = 512
p = np.random.rand(N)
p = p/np.sum(p)

with open('probabilities.txt', 'w') as out:
    for x in p:
        out.write('%f\n' % x)
