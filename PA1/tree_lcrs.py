class CellSpaceItem:
  leftmostchild = None
  label = None 
  rightsibling = None
  def __init__(self, leftmostchild=None, label=None, rightsibling=None ):
    self.leftmostchild = leftmostchild
    self.label = label 
    self.rightsibling = rightsibling
    
class TreeLCRS:
  relativeIndex = 0
  ORIG_MAX_NODES = 10 #Used for resetting in make null
  MAX_NODES = ORIG_MAX_NODES
  #Use built in list ADT
  #The stoarge of items in the cellspace is not important
  #The ADT exists in the connections between cells
  cellspace = [None] *  MAX_NODES
  root = 0 #default root index at 0
  
  def __init__(self):
    self.relativeIndex = 0
    self.cellspace = [None] *  self.MAX_NODES
    self.ORIG_MAX_NODES = 10 #Used for resetting in make null
    self.MAX_NODES = self.ORIG_MAX_NODES
    self.root = 0 #default root index at 0
      
  def create(self,i,newLabel,treelist=[]):
    if i != len(treelist):
      print "TreeLCRS.create: Unequal sizes passed"
      return None
      
    #Create a new tree to work with
    newTree = TreeLCRS()
    #Initialize the root node
    newTree.cellspace[0] = CellSpaceItem()
    newTree.cellspace[0].label = newLabel
    if i ==0:
      return newTree
    
    #For each incoming tree
    for t in range(0,i): 
      #for each node in that trees cellspace
      for cell in range(0,treelist[t].MAX_NODES):
	#Increment the values stored to reflect the future
	#appended positions
	if treelist[t].cellspace[cell] is not None:
	  if treelist[t].cellspace[cell].leftmostchild is not None:
	    treelist[t].cellspace[cell].leftmostchild = treelist[t].cellspace[cell].leftmostchild + newTree.MAX_NODES
	  if treelist[t].cellspace[cell].rightsibling is not None:
	    treelist[t].cellspace[cell].rightsibling = treelist[t].cellspace[cell].rightsibling + newTree.MAX_NODES
      
      #Once the values have been changed, append the lists
      newTree.cellspace = newTree.cellspace + treelist[t].cellspace
      #Update rightsibling
      if t <i-1:
	newTree.cellspace[newTree.MAX_NODES].rightsibling = newTree.MAX_NODES + treelist[t].MAX_NODES
      #Updates max nodes for this new tree
      newTree.MAX_NODES = newTree.MAX_NODES + treelist[t].MAX_NODES
      
    #Link the first tree as the leftmost child
    newTree.cellspace[0].leftmostchild = self.MAX_NODES
    #print "returning tree", newTree.cellspace[0].label, newTree.MAX_NODES
    return newTree

        
  def recursiveparent(self,parent, leftmostchild, nodeToFind):
    if leftmostchild is None:
      return None
      
    if nodeToFind == leftmostchild:
      return parent
      
    if self.cellspace[leftmostchild] is not None:
      #Start checking the children
      it = self.cellspace[leftmostchild].rightsibling
      while it is not None:
	if it == nodeToFind:
	  return parent
	it = self.cellspace[it].rightsibling
      
      #Checked all the children
      #Recursively check all children's children
      it = self.cellspace[leftmostchild].leftmostchild
      while it is not None:
	rv = self.recursiveparent(leftmostchild, it, nodeToFind)
	if rv is not None:
	  return rv - self.relativeIndex
	it = self.cellspace[it].rightsibling
      return None
    
  #This is similar to the previous function in the list
  #Parent isn't readily stored so we need to search the tree
  def parent(self, nodeIndex):
    if nodeIndex == 0:
      #Root node
      return None
    #Loop through cellspace until
    #Start at root
    if self.cellspace[0] is not None:
      return self.recursiveparent(0, self.cellspace[0].leftmostchild, nodeIndex) - self.relativeIndex
    
  def leftmost_child(self, nodeIndex):
    if nodeIndex is not None:
      if nodeIndex < self.MAX_NODES:
	if self.cellspace[nodeIndex] is not None:
	  if self.cellspace[nodeIndex].leftmostchild is not None:  
	    return self.cellspace[nodeIndex].leftmostchild - self.relativeIndex
    return None
	
  def right_sibling(self, nodeIndex):
    if nodeIndex is not None:
      if nodeIndex < self.MAX_NODES:
	if self.cellspace[nodeIndex] is not None:
	  if self.cellspace[nodeIndex].rightsibling is not None:
	    return self.cellspace[nodeIndex].rightsibling - self.relativeIndex
    return None
	
  def label(self, nodeIndex):
    if nodeIndex is not None:
      if self.cellspace[nodeIndex] is not None:
	return self.cellspace[nodeIndex].label
    return None
    
  #root already used as variable name  
  def root_node(self):
    return self.root - self.relativeIndex
      
  def printtree(self):
    print "Index:\t\tLeftmost Child:\t\tLabel:\t\tRight Sibling:"
    for i in range(0, self.MAX_NODES):
      if self.cellspace[i] is not None:
	print i,"\t\t",self.leftmost_child(i),"\t\t\t",self.label(i),"\t\t",self.right_sibling(i)
    
  def makenull(self):
    self.cellspace = [None] *  self.MAX_NODES
    self.MAX_NODES = self.ORIG_MAX_NODES
    self.root = 0 #default root index at 0
    
  def locate(self,label):
    for i in range(0, self.MAX_NODES):
      if self.cellspace[i] is not None:
	if self.cellspace[i].label == label:
	  return i
    return None
  
  
  
  
  
  
  
  
  
  
  
  
  
  
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
    
    
  
  