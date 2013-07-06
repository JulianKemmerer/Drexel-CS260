#!/usr/bin/env python


from array import *
from list_array import *

print "\n\n\n\n=============Dijkstra's Algorithm==============\n\n\n\n" 


print "The purpose of this program is to trace Dijkstra's algorithm using partially ordered tree as a priority queue and linked adjacency lists as the representation of the graph." 

print "\n\n\n"

x=ListArray()
x.insert(1,x.first())
x.insert([5,6],x.first())
x.insert(2,x.first())
x.insert([4,5],x.first())
x.insert(2,x.first())
x.insert([3,2],x.first())
x.insert(10,x.first())
x.insert([1,6],x.first())
x.insert(8,x.first())
x.insert([1,5],x.first())
x.insert(5,x.first())
x.insert([1,4],x.first())
x.insert(1,x.first())
x.insert([1,3],x.first())
x.insert(1,x.first())
x.insert([1,2],x.first())

print "This is the original tree [(start node),(end node),(distance)]\n\n"

x.printlist()
print "\n\n"
print "For each iteration, it should take the shorest path and add it to the set of nodes you are using. Then it should update D so that the shortest distances are represented.\n\n" 

S=[1]
D=["","","","",""]
for i in range( 2 , 7):
	D[i-2] = x.retrieve(x.locate([1,i])+1)
print"here are the node distances from 1, to 1-6:",D

minimum=D[1]
for i in range(1,6):
	smallestNodeIndex=x.retrieve(x.locate(min(D))-1)[1]
	S.append(smallestNodeIndex)
	smallest=min(D)
	D.remove(min(D))
	for vertex in D:
		if x.retrieve(x.locate([smallest,vertex])+1) != None:
			if vertex>smallest+x.retrieve(x.locate([smallest,vertex])+1):
				vertex=smallest+x.retrieve(x.locate([smallest,vertex])+1)
		print "Updated D:",D
		print "Updated S:",S

