#!/usr/bin/env python

#Name from book
class CellType:
  element = None
  next = None
  def __init__(self, element=None, next=None): 
    self.element = element
    self.next = next 

class StackPointer:
  head = CellType()
  #Book has this position iterator thing
  #Not used here
  
  def __init__(self):
    return
 
  def push(self,x):
    #Functions the same as insert(x,head) for list-pointer
    p=self.head
    if self.head.element is not None:
      #Make new node and move head forward
      #copy head values into new node
      new = CellType()
      new.element = self.head.element
      new.next = self.head.next
      #new is now exactly head
      #made head have new values and point to new
      self.head.element = x
      self.head.next = new
      
    #if head is uninitialized
    elif self.head.element is None:
      #Just replace the element value
      self.head.element = x
      
  def empty(self):
    if self.head == None:
      return True
    else:
      return False
  
  def top(self):
    if self.empty():
      print "Stack-Pointer.top: Stack empty."
    else:
      return self.head.element
  
  def pop(self): #Like delete(head)
    p = self.head
    #prev does not exist
    #This must be the start of the list
    #Change the head to point to the second (next element)
    if self.empty():
      print "Stack-Pointer.pop: Stack empty."
    else:
      self.head = p.next    
      
  def makenull(self):
    #Assuming python takes care of memory management
    #Reset the head of the list
    self.head = CellType()
    return
 
  def printstack(self):
    #Loop through and print list
    it = self.head
    while it is not None:
      if it.element is not None:
	print it.element
      it = it.next
    return
    


