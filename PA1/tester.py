#!/usr/bin/env python

from list_array import *
from list_pointer import *
from stack_array import *
from stack_pointer import *
from queue_pointer import *
from tree_loc import *
from tree_lcrs import *
from copy import deepcopy

#x = ListArray()
#x.insert(6,0)
#x.insert(7,0)
#x.insert(8,0)
#x.insert(9,0)
#x.insert(10,0)
#x.delete(2)
#x.printlist()
#print
#print
#print x.next_item(-1)
#x = ListArray()
#x.insert(6,0)
#x.insert(7,0)
#x.printlist()


#WARNING This implementation's END does not function the same as the array's
#END(L) is a pointer to the last cell - from book
#So inserting at end put the element one behind the last element instead of at the end of the list
#I think this is stupid but it is what the book says
#Inserting at head allows for a reverse order list

#y = ListPointer()
#y.insert(3,y.head)
##y.printlistdebug()
#y.insert(4,y.head)
##y.printlistdebug()
#y.insert(5,y.head)
##y.printlistdebug()
#y.insert(6,y.head)
#y.printlist()
#print 
#print
#y.delete(y.locate(3))
#y.delete(y.locate(9))
#y.printlist()

#print
#print y.retrieve(y.locate(6))

#z = StackArray()
#z = StackPointer()
#z.push(10)
#z.push(9)
#z.push(8)
#z.push(7)
#z.push(6)
#z.printstack()
#print
#print
#print z.top()
#z.pop()
#print z.top()
#z.pop()
#print z.top()
#z.pop()
#print z.top()
#z.pop()
#print z.top()
#z.pop()
#print z.top()
#z.pop()
#print z.top()
#z.pop()
#print z.top()
#print
#print
#z.makenull()
#z.printstack()

#q = QueuePointer()
#q.enqueue(10)
#q.enqueue(9)
#q.enqueue(8)
#q.enqueue(7)
#q.printqueue()
#print
#print
#print q.frontelement()
#print
#print
#print q.frontelement()
#q.dequeue()
#print q.frontelement()
#q.dequeue()
#print q.frontelement()
#q.dequeue()
#print q.frontelement()
#q.printqueue()

##Wrote addNode before create so...ignore or use for debug
#t=TreeLOC()
#t.addNode(t.root,1)
#t.addNode(t.root,2)
#t.addNode(t.root,3)
#t.addNode(t.root,4)
##t.makenull()
#t.addNode(t.root.children.retrieve(t.root.children.first()),11)
#t.printtree()
#print
#print 
#print "Root at:", t.root.children.retrieve(t.root.children.first())
#print "Parent found to be:", t.parent(t.root.children.retrieve(t.root.children.first()))
#print 
#print
#print "Leftmost child of root:", t.leftmost_child(t.root)
#print "Leftmost child of t.root.children.retrieve(t.root.children.first()) 's element :", t.leftmost_child(t.root.children.retrieve(t.root.children.first())).element
#print
#print
#print "Right sibling of root:", t.right_sibling(t.root_node())
#print "Right sibling of t.root.children.retrieve(t.root.children.first()) 's element:", t.label(t.right_sibling(t.root.children.retrieve(t.root.children.first())))
#print
#print
#t1=TreeLOC()
#t2=TreeLOC()
#t3=TreeLOC()
#rootTree = TreeLOC()
#t1 = t1.create(0,1)
#t2 = t2.create(0,2)
#t3 = t3.create(0,3)
#treelist = [t1,t2,t3]
#rootTree = rootTree.create(len(treelist),10,treelist)
#rootTree.printtree()

#t=TreeLCRS()
#t.addNode(t.root,1)
#t.addNode(t.root,2)
#t.addNode(t.root,3)
#t.addNode(t.root,4)
##t.makenull()
#t.addNode(t.root.children.retrieve(t.root.children.first()),11)
#t.printtree()
#print
#print 
#print "Root at:", t.root.children.retrieve(t.root.children.first())
#print "Parent found to be:", t.parent(t.root.children.retrieve(t.root.children.first()))
#print 
#print
#print "Leftmost child of root:", t.leftmost_child(t.root)
#print "Leftmost child of t.root.children.retrieve(t.root.children.first()) 's element :", t.leftmost_child(t.root.children.retrieve(t.root.children.first())).element
#print
#print
#print "Right sibling of root:", t.right_sibling(t.root_node())
#print "Right sibling of t.root.children.retrieve(t.root.children.first()) 's element:", t.label(t.right_sibling(t.root.children.retrieve(t.root.children.first())))
#print
#print
#t1=TreeLCRS()
#t2=TreeLCRS()
#t3=TreeLCRS()
#t4=TreeLCRS()
#t1_3 = TreeLCRS()
#t1 = t1.create(0,1)
#t2 = t2.create(0,2)
#t3 = t3.create(0,3)
#t4 = t4.create(0,4)
#treelist = [t1,t2,t3]
#t1_3 = t1_3.create(len(treelist),12,treelist)
#t1_3.printtree()
#print
#print
#t=TreeLCRS()
#treelist = [t1_3,t4]
#t = t.create(len(treelist),123,treelist)
#t.printtree()
#print "Parent of node index 30:", t.parent(30)


#Brian T's test
#A= TreeLOC()
#B=TreeLOC()
#C=TreeLOC()
#D=TreeLOC()
#E = TreeLOC()
#F=TreeLOC()
#G=TreeLOC()
#H=TreeLOC()
#I=TreeLOC()
#J=TreeLOC()
#K=TreeLOC()
#L=TreeLOC()
#M=TreeLOC()  
#N=TreeLOC() 
#M=M.create(0,M)
#N=N.create(0,N)
#D=D.create(0,D)
#F=F.create(0,F)
#L=L.create(0,L)
#I=I.create(2,[M,N])
#G=G.create(2,[J,K]) 
#H=H.create(1,[L])
#C=C.create(3,[F,G,H])
#A=A.create(2,[B,C])
'''
X = TreeLOC() 
Y = TreeLOC() 
Z = TreeLOC()

X = X.create(0,"X Label")
Y = Y.create(0,"Y Label")
treelist=[X,Y]
Z = Z.create(len(treelist),"Z Label",treelist)
Z.printtree()
'''


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
		
		
def buildTreeNew(type, n):
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
		#start from bottom of tree
		 
		
		
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
	
tree = buildTree(TreeLOC, 3)

tree.printtree()
raw_input()
p = tree.root_node()
p = tree.leftmost_child(p)
#print
#print p
#p = tree.right_sibling(p)
#print p
#p = tree.right_sibling(p)
#print p
#p = tree.right_sibling(p)
#print p
traverse(tree, tree.root)






