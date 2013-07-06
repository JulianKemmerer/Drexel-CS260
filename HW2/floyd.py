#!/usr/bin/env python

'''
procedure Floyd ( var A: array[1..n, 1..n]
of real;
C: array[1..n, 1..n] of real );
{ Floyd computes shortest path matrix A given arc cost matrix C }
var
i, j, k: integer;
begin
for i := 1 to n do
for j := 1 to n do
A[i, j] := C[i, j];
for i:= 1 to n do
A[i, i] := 0;
for k:= 1 to n do
for i := 1 to n do
for j:= 1 to n do
if A[i, k] + A[k, j] < A
[i, j] then
A[i, j] := A[i, k] + A[k,
j]
end; { Floyd }
'''

C=[[9999]*6]*6

C[0][1]=3
C[0][2]=4
C[0][5]=5

C[1][2]=1
C[1][5]=1

C[2][3]=2

C[3][1]=3

C[4][3]=3
C[4][5]=2

C[5][3]=2
  
A=[[9999]*6]*6

i=0
j=0
k=0

for i in range(0,6):
  for j in range(0,6):
    A[i][j] = C[i][j]
    
#for i in range(0,6):
 # A[i][i]=0

for k in range(0,6):
  for i in range(0,6):
    for j in range(0,6):
      print A
      if (A[i][k] + A[k][j]) < A[i][j]:
	A[i][j] = A[i][k] + A[k][j]
	
#print A
for i in range(0,6):
    print "ROW:",i, "\t",A[i][0] , A[i][1],A[i][2],A[i][3],A[i][4],A[i][5]



