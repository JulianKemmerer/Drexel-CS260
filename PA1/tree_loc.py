# PARENT, LEFTMOST_CHILD, RIGHT_SIBLING, LABEL, CREATEi (i=0,1,2,3), ROOT, MAKENULL.
from list_pointer import *

#All the functions of the TreeLOC class return TreeNode's when appropriate
class TreeNode:
  element = None
  children = None #list of TreeNodes
  def __init__(self, element=None, children=None):
    self.element = element
    self.children = children 

#Rather than a single list of linked lists
#Use lists of nodes that have lists of children
#Same concept just added another dimension that comes
#naturally to tress
class TreeLOC:
  root = TreeNode()
  
  def __init__(self):
    self.root = TreeNode()
  
  #Wrote this before writing the create functions  - use for debugging if you want
  def addNode(self,parentNode,element):
    #print "Adding element", element, "to node", parentNode
    newNode = TreeNode(element)
    if parentNode is not None:
      if parentNode.children is None:
	#make a new list
	parentNode.children = ListPointer()
      #print "Inserting new node:", newNode, "into list:", parentNode.children, "within parent:", parentNode
      parentNode.children.insert(newNode,parentNode.children.first())
      #print "List contents after insert:"
      #parentNode.children.printlist()

      
  def recursiveparent(self,parent, children, nodePtrFind):
    print "finding child", nodePtrFind, "in parent", parent
    #Start searching at the first child
    it = children.first()
    #Loop through each child and check if node in question
    while it is not None:
      if it.element==nodePtrFind:
	return parent
      it = it.next
    #If not found by this point start searching the children of each child
    rv = None
    #For each child
    #Start searching at the first child
    it = children.first()
    #Loop through each child and check if node in question
    while it is not None:
      if it.element is not None:
	if it.element.children is not None:
	  #Get children list
	  newChildrenList = it.element.children
	  rv = self.recursiveparent(it.element,newChildrenList, nodePtrFind)
	  if rv is not None:
	    return rv
      it = it.next
    #Return return value (may be None)
    return rv
  
  #This is similar to the previous function in the list
  #Parent isn't readily stored so we need to search the tree
  def parent(self, nodePtr):
    print "Looking for parent of:", nodePtr
    it = self.root
    if nodePtr == self.root:
      return None
    return self.recursiveparent(it,it.children, nodePtr)
    
  #Will be the start of the linked list that is the children of that node  
  def leftmost_child(self, nodePtr):
    if nodePtr is not None:
      if nodePtr.children is not None:
	return nodePtr.children.first().element
      else:
	return None # no children
	
  def right_sibling(self, nodePtr):
    #Get the parent
    parentNode = self.parent(nodePtr)
    if parentNode is not None:
      #Get the children list
      childrenList = parentNode.children
      #Find current node
      curNode = childrenList.locate(nodePtr)
      #Return the next node
      if childrenList.next_item(curNode) is not None:
	return childrenList.next_item(curNode).element
      else:
	return None
    else:
      return None
      
  # label  = element    
  def label(self, nodePtr):
    if nodePtr is not None:
      return nodePtr.element
    return None
    
  #root already used as variable name  
  def root_node(self):
    return self.root
      
  def printtree(self):
    #Print the root node
    self.recursiveprint(self.root)
    
  def recursiveprint(self,treeNode):
    if treeNode is not None:
      #Print the nodes children
      if treeNode.children is not None:
	print "Node:", treeNode, " w/ element = ", treeNode.element , ". Has Children List:", treeNode.children, "and children:"
	treeNode.children.printlist()
	print
	it = treeNode.children.first()
	
	while it is not None:
	   self.recursiveprint(it.element)
	   it = it.next
      else:
	print "Node:", treeNode, " w/ element = ", treeNode.element , ". Has no children."
	
  def makenull(self):
    self.root = TreeNode()
  
  
  #CREATEi(v, T1, T2, . . . , Ti) is one of an infinite family of functions, one for
  #each value of i = 0, 1, 2, . . .. CREATEi makes a new node r with label v and
  #gives it i children, which are the roots of trees T1, T2, . . . , Ti, in order from
  #the left. The tree with root r is returned. Note that if i = 0, then r is both a leaf
  #and the root.
  #Accepts python list object storing trees
  #this passed list is not important to the benchmark times
  #so it is fine to use built in object
  #i can be passed as len(treelist)
  def create(self,i,newLabel,treelist=[]):
    #make new node
    newNode = TreeNode(newLabel)
    #Make that new node have a blank children list
    newNode.children = ListPointer()
    if i != len(treelist):
      print "TreeLOC.create: Unequal sizes passed. i=", i, "len(treelist)=",len(treelist)
      return None
      
    if i==0:
      #Create a new tree and modify root
      newTree = TreeLOC()
      newTree.root.element = newLabel
      return newTree
    
    for count in range(0,i):
      #Add the root of that tree as a child of the newNode
      newNode.children.insert(treelist[count].root_node(), newNode.children.first())
    
    #new node now has children being the passed in trees
    rv = TreeLOC()
    rv.root = newNode
    return rv
    
    
  
  