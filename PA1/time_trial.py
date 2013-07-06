#!/usr/bin/env python
#
#   This program performs time trials with the data structures that we implemented.
#	Trials are done using the Python 'timeit' library.  Tests are run 10 times and
#	the times are averaged to get the final run time for the trial.
#
#   For lists, the following operations are tested on both of our implementations,
#   as well as their built-in Python equivalent:
#
#        - iterated insertion (front)
#        - iterated insertion (back)
#        - traversal
#        - iterated deletion (front)
#        - iterated deletion (back)
#
#    Tree traversal is also tested for both of our tree implementations.
#

from timeit import timeit, Timer
from sys import stdout
from copy import deepcopy

# Import our data types
from list_array import *
from list_pointer import *
from tree_loc import *
from tree_lcrs import *


def main():
	
	#======================================================================
	# List: iterated insertion - front
	#======================================================================
	
	table = {
		'Data Size' : [],
		'List (Array)' : [],
		'List (Pointer)' : [],
		'List (Python)' : []
	}
	
	for data_size in xrange(1, 10):
		table['Data Size'].append(data_size)
		
		# Array implementation
		def arrTest():
			array = ListArray()
			for i in xrange(0, data_size):
				array.insert(i, 0)
		t = Timer(arrTest)
		table['List (Array)'].append('{0:.8f}'.format(t.timeit(10)))
		
		# Pointer implementation
		def pointTest():
			pointer = ListPointer()
			for i in xrange(0, data_size):
				pointer.insert(i, pointer.head)
		t = Timer(pointTest)
		table['List (Pointer)'].append('{0:.8f}'.format(t.timeit(10)))
		
		# Built-in implementation
		def pyTest():
			l = []
			for i in xrange(0, data_size):
				l.insert(0, i)
		t = Timer(pyTest)
		table['List (Python)'].append('{0:.8f}'.format(t.timeit(10)))
		
	# Output the results
	print 'List: Iterated Insertion - Front\n'
	printTable(table)
	print '\n'
		
	
	#======================================================================
	# List: iterated insertion - back
	#======================================================================
	
	table = {
		'Data Size' : [],
		'List (Array)' : [],
		'List (Pointer)' : [],
		'List (Python)' : []
	}
	
	for data_size in xrange(1, 11):
		table['Data Size'].append(data_size)
		
		# Array implementation
		def arrTest():
			array = ListArray()
			for i in xrange(0, data_size):
				array.insert(i, array.last + 1)
		t = Timer(arrTest)
		table['List (Array)'].append('{0:.8f}'.format(t.timeit(10)))
		
		# Pointer implementation
		def pointTest():
			pointer = ListPointer()
			for i in xrange(0, data_size):
				pointer.insert(i, pointer.end())
		t = Timer(pointTest)
		table['List (Pointer)'].append('{0:.8f}'.format(t.timeit(10)))
		
		# Built-in implementation
		def pyTest():
			l = []
			for i in xrange(0, data_size):
				l.append(i)
		t = Timer(pyTest)
		table['List (Python)'].append('{0:.8f}'.format(t.timeit(10)))
		
	# Output the results
	print 'List: Iterated Insertion - Back\n'
	printTable(table)
	print '\n'
	
	
	#======================================================================
	# List: traversal
	#======================================================================
	
	table = {
		'Data Size' : [],
		'List (Array)' : [],
		'List (Pointer)' : [],
		'List (Python)' : []
	}
	
	for data_size in xrange(1, 11):
		table['Data Size'].append(data_size)
		
		# Array implementation
		array = ListArray()
		for i in xrange(0, data_size):
			array.insert(i, array.last + 1)
		def arrTest():
			last_next = None
			i = 0
			while i != last_next:
				try:
					x = array.retrieve(i)
				except:
					break
				last_next = i
				i = array.next_item(i)
		t = Timer(arrTest)
		table['List (Array)'].append('{0:.8f}'.format(t.timeit(10)))
		
		# Pointer implementation
		pointer = ListPointer()
		for i in xrange(0, data_size):
			pointer.insert(i, pointer.end())
		def pointTest():
			p = pointer.head
			while p is not None:
				x = pointer.retrieve(p)
				p = pointer.next_item(p)
		t = Timer(pointTest)
		table['List (Pointer)'].append('{0:.8f}'.format(t.timeit(10)))
		
		# Built-in implementation
		l = []
		for i in xrange(0, data_size):
			l.append(i)
		def pyTest():
			for i in xrange(0, len(l)):
				x = l[i]
		t = Timer(pyTest)
		table['List (Python)'].append('{0:.8f}'.format(t.timeit(10)))
		
	# Output the results
	print 'List: Traversal\n'
	printTable(table)
	print '\n'
	
	
	#======================================================================
	# List: iterated deletion - front
	#======================================================================
	
	table = {
		'Data Size' : [],
		'List (Array)' : [],
		'List (Pointer)' : [],
		'List (Python)' : []
	}
	
	for data_size in xrange(1, 11):
		table['Data Size'].append(data_size)
		
		# Array implementation
		array = ListArray()
		for i in xrange(0, data_size):
			array.insert(i, array.last + 1)
		def arrTest():
			while True:
				try:
					array.delete(0)
				except:
					break
		table['List (Array)'].append('{0:.8f}'.format(t.timeit(10)))
		
		# Pointer implementation
		pointer = ListPointer()
		for i in xrange(0, data_size):
			pointer.insert(i, pointer.end())
		def pointTest():
			while True:
				try:
					pointer.delete(pointer.head)
				except:
					break
		t = Timer(pointTest)
		table['List (Pointer)'].append('{0:.8f}'.format(t.timeit(10)))
		
		# Built-in implementation
		l = []
		for i in xrange(0, data_size):
			l.append(i)
		def pyTest():
			while len(l) > 0:
				del l[0]
		t = Timer(pyTest)
		table['List (Python)'].append('{0:.8f}'.format(t.timeit(10)))
	
	# Output the results
	print 'List: Iterated Deletion - Front\n'
	printTable(table)
	print '\n'
	
	
	#======================================================================
	# List: iterated deletion - back
	#======================================================================
	
	table = {
		'Data Size' : [],
		'List (Array)' : [],
		'List (Pointer)' : [],
		'List (Python)' : []
	}
	
	for data_size in xrange(1, 11):
		table['Data Size'].append(data_size)
		
		# Array implementation
		array = ListArray()
		for i in xrange(0, data_size):
			array.insert(i, array.last + 1)
		def arrTest():
			while True:
				try:
					array.delete(array.end() -1)
				except:
					break
		table['List (Array)'].append('{0:.8f}'.format(t.timeit(10)))
		
		# Pointer implementation
		pointer = ListPointer()
		for i in xrange(0, data_size):
			pointer.insert(i, pointer.end())
		def pointTest():
			while True:
				try:
					pointer.delete(pointer.end())
				except:
					break
		t = Timer(pointTest)
		table['List (Pointer)'].append('{0:.8f}'.format(t.timeit(10)))
		
		# Built-in implementation
		l = []
		for i in xrange(0, data_size):
			l.append(i)
		def pyTest():
			while len(l) > 0:
				del l[-1]
		t = Timer(pyTest)
		table['List (Python)'].append('{0:.8f}'.format(t.timeit(10)))
		
	# Output the results
	print 'List: Iterated Deletion - Back\n'
	printTable(table)
	print '\n'
	
	
	#======================================================================
	# Tree traversal
	#======================================================================
	
	table = {
		'Data Size' : [],
		'LOC' : [],
		'LCRS' : []
	}
	
	for data_size in xrange(1, 11):
		table['Data Size'].append(data_size)
		
		# Create the trees
		loc = buildTree(TreeLOC, data_size)
		lcrs = buildTree(TreeLCRS, data_size)
		
		# Run the timing tests for the LOC tree  BROKEN!!!!
		'''
		t = Timer(
			stmt = 'traverse(t, t.root)',
			setup = 'from __main__ import traverse, buildTree, TreeLOC; t = buildTree(TreeLOC, ' + str(data_size) + ')'
		)
		table['LOC'].append('{0:.8f}'.format(t.timeit(10)))
		'''
		
		# Run the timing tests for the LCRS tree
		t = Timer(
			stmt = 'traverse(t, t.root)',
			setup = 'from __main__ import traverse, buildTree, TreeLCRS; t = buildTree(TreeLCRS, ' + str(data_size) + ')'
		)
		table['LCRS'].append('{0:.8f}'.format(t.timeit(10)))
	
	# Output the results
	print 'Tree traversal\n'
	printTable(table)
	print '\n'
	


def buildTree(type, n):
	'''
	Generate a tree of degree 3 and height 'n'
	'''
	
	# Template for a node containing three leaves
	leaf_list = [
		type().create(0, 1),
		type().create(0, 2),
		type().create(0, 3)
	]
	leaf_temp = type().create(3, 0, leaf_list)
	
	# Loop to build the tree
	if n == 1:
		return leaf_temp
	else:
		tree = None
		for _ in xrange(1, n):
			tree = type().create(3, 0, [deepcopy((tree, leaf_temp)[tree is None])]*3)
		return tree
	
def traverse(tree, p):
	'''
	Traverse a tree; leaves are counted along the way, but this isn't used
	'''
	
	n = 0
	lmc = tree.leftmost_child(p)
	rs = tree.right_sibling(p)
	
	if lmc is not None:
		n += traverse(tree, lmc)
	if rs is not None:
		n += traverse(tree, rs)
	if lmc is None and rs is None:
		return 1 + n
	else:
		return n


def printTable(x):
	'Accept a dictionary of arrays and print the data as a table'
	
	# Check that the data structure is
	if type(x) is not dict:
		raise('Invalid data type received')
	for key in x:
		if type(x[key]) is not list:
			raise('Invalid data type received')
	
	# Determine column widths
	widths = {}
	for key in sorted(x):
		widths[key] = len(key) + 2
		for item in x[key]:
			l = len(str(item))
			if l > widths[key]:
				widths[key] = l
	
	# Print headers
	for key in sorted(x):
		stdout.write(' %s ' % str(key).ljust(widths[key]))
	print
	
	# Print underlines
	for key in sorted(widths):
		stdout.write((widths[key] * '-') + '  ')
	print
		
	# Print data
	row = 0
	go = True
	while go:
		go = False
		for key in sorted(x):
			try:
				if bool(x[key][row]):
					go = True
					break
			except:
				pass
		if go:
			for key in sorted(x):
				try:
					stdout.write(' ' + str(x[key][row]).ljust(widths[key] + 1))
				except:
					stdout.write((widths[key] + 2) * ' ')
		print
		row += 1

if __name__ == '__main__':
	main()
	