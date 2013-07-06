/* Problem Description:

Floyd's algorithm (6.4) with the option of recovering the paths. 
Test your implementation on the graph of problem 6 of review 2.

A[1,2]=4, A[1,3]=1, A[1,4]=5, A[1,5]=8, A[1,6]=10, 
A[3,2]=2, A[4,5]=2, A[5,6]=1. 

Compile and run with 
g++ Problem8.cpp -o Problem8 && ./Problem8

Put all code in one file for easier submission
*/

#define NODES 6
#define INF 99999

#include <iostream>
using namespace std;

//Graph object as adjacency matrix
//Easier than passing a 2D array around
class Graph{
public:
  Graph();
  int C[NODES][NODES];  
};

//Graph Implementation
Graph::Graph()
{
  //Init all distances as inf
  for(int i = 0; i<NODES;i++)
  {
    for(int j = 0; j<NODES;j++)
    {
      C[i][j]=INF;
    }
  }
}

int main()
{
  Graph g;
  //Fill in values given from review problem
  //Subtract one from indices as this graph is zero indexed
  g.C[0][1]=4;
  g.C[0][2]=1; 
  g.C[0][3]=5;
  g.C[0][4]=8;
  g.C[0][5]=10;
  g.C[2][1]=2; 
  g.C[3][4]=2; 
  g.C[4][5]=1;
  
  //Begin floyds algorithm
  
  int i,j,k;
  int A[NODES][NODES];
  int P[NODES][NODES]; //P previous point of each shortest path 
  
  //Copy C into A
  for(i=0; i<NODES; i++)
  {
    for(j=0; j<NODES; j++)
    {
      A[i][j] = g.C[i][j];
      P[i][j] = -2; //No route exists default
    }
  }
  
  //Cost from node to self is zero
  for(i=0; i<NODES; i++)
  {
    A[i][i] = 0;
  }
  
  //Loop to handle direct connections
  for(i=0; i<NODES; i++)
  {
    for(j=0; j<NODES; j++)
    {
      if( A[i][j] < INF)
      {
	if(i!=j)
	{
	  P[i][j]=-1; //A direct connection exits
	}
      }	
    }
  }
  
  //Main O(n^3) loop
  for(k=0; k<NODES; k++)
  {
    for(i=0; i<NODES; i++)
    {
      for(j=0; j<NODES; j++)
      {
	if( (A[i][k] + A[k][j]) < A[i][j])
	{
	  A[i][j] = A[i][k] + A[k][j];
	  P[i][j]=k;
	}	
      }
    }
  }
  
  //Print results
  cout << "ONE INDEXED!" << endl;
  cout << "Zero Signifies a Direct Connection" << endl;
  cout << "Negative One Signifies No Possible Connection" << endl;
  cout << "\t" << "P[][1]\t" << "P[][2]\t" << "P[][3]\t" << "P[][4]\t" << "P[][5]\t" << "P[][6]\t"<< endl;
  for(i=0; i< NODES; i++)
  {
    cout << "P["<< i +1<< "][]\t";
    
    for(j=0; j <NODES; j++)
    {
      cout << P[i][j] +1 << "\t";
    }
    cout << endl;
  }
  
  return 0;
}