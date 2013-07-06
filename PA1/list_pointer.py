#!/usr/bin/env python

#WARNING This implementation's END does not function the same as the array's
#END(L) is a pointer to the last cell - from book
#So inserting at end put the element one behind the last element instead of at the end of the list
#I think this is stupid but it is what the book says

from array import *

#Name from book
class CellType:
  element = None
  next = None
  def __init__(self, element=None, next=None): 
    self.element = element
    self.next = next 

class ListPointer:
  head = CellType()
  def __init__(self):
    self.head = CellType()
  #Book has this position iterator thing
  #Not used here
  
  def previous(self,p):
    it = self.head
    while it is not None:
      if it.next == p:
	return it
      it = it.next
    return None
  
  def insert(self,x,p): 
    #For some reason this became more complicated than needed
    #If there are no elements inserting at END changes the header
    #If there is only one element in the list inserting at END is like append
    #If p is END(L), then L becomes a1, a2, . . . , an, x
    if p is not None:
      
      #Special case, if inserting at hear
      if p==self.head:
	#if head is initialized
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
      
      else:
	#Not special case proceed as normal
	new = CellType()
	new.element = x
	#if a previous cell exists link from it to the new cell
	prev = self.previous(p);
	if prev is not None:
	  prev.next = new;
	#Regardless link to item passed as position
	new.next = p
    else:
      print "ListPointer.insert: Passed null pointer"
    return
      

  def locate(self,x):
    #Returns the pointer to first occurance of x
    #If x does not appear at all, then END(L) is returned.
    it = self.head
    while it is not None:
      if it.element == x:
	return it
      it = it.next
    #This goes against what the book says
    #If you return end, and end is said to be:
    #END(L) is a pointer to the last cell
    #Then you think you found the item in the last cell?
    #Return null instead
    return None
   
    
  def retrieve(self,p):
    # I think this is trivial as
    # p contains a element field?
    if p is not None:
      return p.element
    else:
      raise("ListPointer.retrieve: Passed null pointer")
    
    
  def delete(self,p):
    #Ex.
    #          a -> p -> c
    # make a next point to c
    # make prev.next point to p.next
    # I assume python is smart enough
    # not to cause a memory leak :-)
    if p is not None:
      prev = self.previous(p)
      #if prev exists
      if prev is not None:
	#Make prev.next point to p.next
	prev.next = p.next
      else:
	#prev does not exist
	#This must be the start of the list
	#Change the head to point to the second (next element)
	self.head = p.next
    else:
      raise("ListPointer.delete: Passed null pointer")
   
  #'next' is already defined in python, I don't know how to get around that
  def next_item(self,p):
    if p is not None:
      return p.next
    return None
    
  def makenull(self):
    #Assuming python takes care of memory management
    #Reset the head of the list
    self.head = CellType()
    return
  
  def first(self):
    return self.head
    
  def printlist(self):
    #Loop through and print list
    it = self.head
    while it is not None:
      if it.element is not None:
	print "Node:", it, "\tElement:",it.element
      it = it.next
    return

  def end(self):
    #END(L) is a pointer to the last cell - from book
    #Loop through list until end
    it = self.head
    while it.next is not None:
      it = it.next
    return it
    


