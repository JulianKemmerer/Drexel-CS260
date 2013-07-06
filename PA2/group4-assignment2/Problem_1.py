#
#	Programming Assignment 2
#
#	Problem 1  (15 Points)
#
#	Huffman algorithm (3.4). For a given collection of characters and probabilities
#	your program should create the Huffman tree and print out the codes for all the
#	characters. Test your implementation on data provided in problem 3.20.
#

# Native binary tree implementation
from heapq import heapify, heappop, heappush

def printCodes(t, code_str = ''):
	'''
	Accept the root node of a 'heapq' tree and print the Huffman codes.
	This function uses recursion to build the codes strings.
	'''
	if len(t) < 3:
		print('%s: %s' % (t[1], code_str))
	else:
		printCodes(t[1], code_str + '0')
		printCodes(t[2], code_str + '1')

# Initialize the input (data taken from 3.20)
tree = [
	[0.07, 'a'],
	[0.09, 'b'],
	[0.12, 'c'],
	[0.22, 'd'],
	[0.23, 'e']
]
	
# Convert the input into a binary tree
heapify(tree)

# Sort the tree into a valid Huffman tree.
# To do this, pop two nodes, then push them back into the tree under a
# node with the combined total probability
while len(tree) > 1:
	x = heappop(tree)
	y = heappop(tree)
	total_prob = x[0] + y[0]
	heappush(tree, (total_prob, x, y))

# Output
printCodes(tree[0])
