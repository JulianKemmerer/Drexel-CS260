#!/usr/bin/env python

from queue_pointer import *



q = QueuePointer()
print "Empty Queue:"
q.printqueue()
print "Enqueueing..."
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print "Populated Queue:"
q.printqueue()
print "Dequeue...and go too far:"
print "Front element:" , q.frontelement()
print "Dequeue."
q.dequeue()
print "Front element:" , q.frontelement()
print "Dequeue."
q.dequeue()
print "Front element:" , q.frontelement()
print "Dequeue."
q.dequeue()
print "Front element:" , q.frontelement()
print "Dequeue."
q.dequeue()
print "Front element:" , q.frontelement()
print "Dequeue."
q.dequeue()
print "Front element:" , q.frontelement()
print "Dequeue."
q.dequeue()
print "Enqueueing again..."
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print "Populated Queue:"
q.printqueue()
print "Dequeue...and go too far:"
print "Front element:" , q.frontelement()
print "Dequeue."
q.dequeue()
print "Front element:" , q.frontelement()
print "Dequeue."
q.dequeue()
print "Front element:" , q.frontelement()
print "Dequeue."
q.dequeue()
print "Front element:" , q.frontelement()
print "Dequeue."
q.dequeue()
print "Front element:" , q.frontelement()
print "Dequeue."
q.dequeue()
print "Front element:" , q.frontelement()
print "Dequeue."
q.dequeue()

