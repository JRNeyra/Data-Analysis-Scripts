#########################################################
# Description: This script generates a Huffman code file
# out of a probabilities file in the same folder as this
# script. This scrypt uses the Binary Search Tree data
# structure and recursion algorithms to generate the new
# codeword list.
# Author: Jose Neyra
#########################################################

# Create the node class
class Node:
    left = None
    right = None
    p = 0
    def __init__(self,p,left=None,right=None):
        self.p = p
        self.left = left
        self.right = right


# Read the probability file
with open('probabilities.txt', 'r') as inp:
    P = inp.read().splitlines()


# Traverse the graph and output codes
def getCodeWords(c, node):
    if node.left is None:
        codewords.append(c)
    else:
        getCodeWords(c+'0', node.left)
        getCodeWords(c+'1', node.right)


# Initialize all leaf nodes
nodes = [Node(float(p)) for p in P]
nodes.sort(key=lambda x: x.p)

# Construct the graph
while len(nodes) > 1:
    n1 = nodes.pop(0)
    n2 = nodes.pop(0)
    n = Node(n1.p+n2.p,n1,n2)
    nodes.append(n)
    nodes.sort(key=lambda x: x.p)

# Initialize Codewords list
codewords = []

getCodeWords('', nodes[0])

with open('codes.txt', 'w') as out:
    for c in codewords:
        out.write('%s\n' % c)
