#!/usr/bin/env python

from array import *

class ListArray:
  #Max length per book definition
  MAX_LENGTH = 100
  #Integer array
  elements = array('i')
  #Equivalent to the last usable index
  last = -1
  
  def __init__(self):
    self.elements = [0]*self.MAX_LENGTH #Init to maxmimum static size
    return
  
  def insert(self,x,p):
    if not(self.last < self.MAX_LENGTH -1) :
      print "List-Array.insert: Array already at maximum size: ", self.MAX_LENGTH
    elif p <=self.last+1 and p>=0:
      #Insert x into p by moving all elements at p or after up by one
      #Start from the end of the list and move towards the back
      for i in range(self.last,p-1,-1): #downto and including p
	self.elements[i+1] = self.elements[i]
      #Put x in
      self.elements[p] = x
      self.last = self.last + 1
    else:
      print "List-Array.insert: Index out of range: ", p, ". Length: ",self.last+1
    return

  def locate(self,x):
    #Returns the index of the first occurance of x
    #If x does not appear at all, then END(L) is returned.
    for i in range(0,self.last+1):
      if self.elements[i]==x:
	  return i;
    #Not found
    return self.end()
    
  def retrieve(self,p):
    if p <=self.last and p>= 0:
      return self.elements[p]
    else:
      raise("List-Array.retrieve: Index out of range: ", p, ". Length: ",self.last+1)
      #The result is undefined if p = END(L) or if L has no position p.
      return
    
  def delete(self,p):
    if p <=self.last and p>= 0:
      #Delete x into p by moving all elements at after p down by 1
      #Start from one after p and go to end of list
      for i in range(p+1,self.last+1):
	self.elements[i-1] = self.elements[i]
      self.last = self.last - 1
    else:
      raise("List-Array.delete: Index out of range: ", p, ". Length: ",self.last+1)
    return
  
  #'next' is already defined in python, I don't know how to get around that
  def next_item(self,p):
    if p < self.last and p >= 0:
      return p+1
    else:
      return self.end()
    
  def previous(self,p):
    if p <= self.last and p > 0:
      return p-1
    else:
      return self.end()
    
  def makenull(self):
    #Take this as re initializing the list?
    self.__init__()
    return
  
  def first(self):
    if self.last >=0:
      return 0
    else:
      return self.end()
    
  def printlist(self):
    #Loop through and print list
    for i in range(0,self.end()):
      print self.elements[i]
    return
    
  def end(self):
    #Return one past the last usable index
    return self.last+1
    


