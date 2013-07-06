#!/usr/bin/env python

from array import *

class StackArray:
  #Max length per book definition
  MAX_LENGTH = 100
  #Integer array
  elements = array('i')
  #Index of the top element of the stack
  #Book says "anchor the bottom of the stack at the bottom
  #(high-indexed end) of the array, and let the stack grow towards the top
  #Top index initialized to one past end
  top_index = MAX_LENGTH #MAX_LENGTH - 1 is first usable index
  
  #Book says you can write in terms of list operations
  #Then they say not to...so I didn't
 
  def __init__(self):
    self.elements = [0]*self.MAX_LENGTH #Init to maxmimum static size
    return
    
  def empty(self):
    if(self.top_index>= self.MAX_LENGTH):
      return True
    else:
      return False
  
  def top(self):
    if self.empty():
      print "Stack-Array.top: Stack empty."
    else:
      return self.elements[self.top_index]
  
  def pop(self):
    if self.empty():
      print "Stack-Array.pop: Stack empty."
    else:
      self.top_index = self.top_index +1
  
  def push(self,x):
    if self.top_index ==0:
      print "Stack-Array.push: Stack full."
    else:
      self.top_index = self.top_index - 1
      self.elements[self.top_index] = x
      
  def makenull(self):
    #Book does it by just resetting the top index counter
    self.top_index = self.MAX_LENGTH
    return
    
  def printstack(self):
    #Loop through and print
    for i in range(self.MAX_LENGTH - 1,self.top_index-1, -1):
      print self.elements[i]
    return
