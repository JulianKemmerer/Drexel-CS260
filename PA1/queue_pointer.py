#!/usr/bin/env python

#Name from book
class CellType:
  element = None
  next = None
  def __init__(self, element=None, next=None): 
    self.element = element
    self.next = next 

class QueuePointer:
  front = CellType()
  rear = CellType()
  
  def __init__(self):
    self.front = CellType()
    self.rear = CellType()
    return
       
  def empty(self):
    if (self.front == None) and (self.rear==None) :
      return True
    elif (self.front.element == None) and (self.rear.element==None):
      return True
    else:
      return False
  
  #Python gives error using .front()
  def frontelement(self):
    if self.empty():
      print "Queue.front: Queue empty."
    else:
      return self.front.element  
      
  #ENQUEUE(x, Q) inserts element x at the end of queue Q
  #Like  INSERT(x, rear)
  def enqueue(self,x):
    #Functions the same as insert(x,rear) for list-pointer
    
    #IF enqueueing into newly empty queue (emptied using dequeue)
    #Reinitilaize
    if (self.rear is None) and (self.front is None):
      self.front = CellType()
      self.rear = CellType()
    
    p=self.rear
    if self.rear.element is not None:
      #Make new node and move forward
      #Copy values into new node
      new = CellType()
      new.element = self.rear.element
      new.next = self.rear.next
      #new is now exactly rear
      #made rear have new values and point to new
      self.rear.element = x
      self.rear.next = new
      if(self.front.next is not None):
	self.front = self.front.next
      
    #if rear is uninitialized
    elif self.rear.element is None:
      #Just replace the element value
      self.rear.element = x
      #rear was uninitized so now that it
      #has an element, front and rear are the same
      self.front = self.rear
  
  #DEQUEUE(Q) deletes the first element of Q
  #Like delete(front)
  def dequeue(self):
    p = self.front
    if self.empty():
      print "QueuePointer.dequeue: Empty queue"
    else:
      #if prev exists
      prev = self.previous(p)
      if prev is not None:
	#Make prev.next point to None (drop front object)
	prev.next = None
	self.front = prev
      else:
	#prev does not exist
	#This must be the start of the list
	self.front = None
	self.rear = None

  def previous(self,p):
    it = self.rear
    while it is not None:
      if it.next == p:
	return it
      it = it.next
    return None
  
  def makenull(self):
    #Assuming python takes care of memory management
    #Reset the front and rear of the list
    self.front = CellType() 
    self.rear = CellType()
    return
    
  def printqueue(self):
    #Loop through and print list
    it = self.rear
    while it is not None:
      if it.element is not None:
	print it.element
      it = it.next
    return
    


