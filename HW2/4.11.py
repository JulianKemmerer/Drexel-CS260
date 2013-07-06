# Script to solve problem 4.11


#!/usr/bin/env python
b=16

def hash(index,k):
  if 2*d[index-1] < b:
    return 2*d[index-1]
  else:
    return (2*d[index-1] - b)^k
    #(2*d[index-1] - b) XOR k
    
def check(d):
  for j in range(1,16): #ints 1 to 15
    pos=[i for i,x in enumerate(d) if x == j]
    if len(pos) !=1:
      return False
  return True

for k in range(0,16):
  d=[-1]*16
  d[1] = 1
  for index in range(2,16):
    d[index] = hash(index,k)

  #Check if proper
  if check(d):
    print "k:",k
    print d

