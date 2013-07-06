/* Problem Description:

Dijkstra's shortest paths algorithm (6.3) 
with the adjacency matrix as the representation of the graph.

A[1,2]=4, A[1,3]=1, A[1,4]=5, A[1,5]=8, A[1,6]=10, 
A[3,2]=2, A[4,5]=2, A[5,6]=1. 

Compile and run with 
g++ Problem6.cpp -o Problem6 && ./Problem6

Put all code in one file for easier submission
*/

#define NODES 6
#define INF 99999

#include <iostream>
#include <vector>
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

//Set object for use in dijkstra
//Did not use just regular vector as object
//Or as public member to prevent improper manipulation
//(like inserting the same things twice)
//And added some extra functions
class Set
{
public:
  Set(int startNode);
  Set();
  int indexof(int toFind);
  void add(int i);
  int elementAt(int index);
  int size();
  
private:
  vector<int> vec;
};
//Set implementation
Set::Set()
{
  //No start node provided
}
Set::Set(int startNode)
{
  //Add node to set
  vec.push_back(startNode);
}
int Set::indexof(int toFind)
{
  int size = vec.size();
  for(int i=0; i< size;i++)
  {
    if(vec[i]==toFind)
    {
      return i;
    }
  }
  return -1;
}
void Set::add(int i)
{
  //No doubles
  if(indexof(i)==-1)
  {
    //Simple append
    vec.push_back(i);
  }
}
int Set::elementAt(int index)
{
  return vec[index];
}
int Set::size()
{
  return vec.size();
}


//Actual start of the main program code

//Make S,w,D and P globals for ease
Set S(0); //Starting at node 1, zero indexed
int D[NODES];
int P[NODES];
int w;

//General helper functions
Set set_not(Set s)
{
  //Return a set filled with all values 0->NODES-1
  //That do not occur in s
  Set returnVal;
  for(int i=0; i< NODES; i++)
  {
    if(s.indexof(i)==-1)
    {
      //Item does not exist in s
      returnVal.add(i);
    }
  }
  return returnVal;
}

int minDNode(Set s)
{
  //Loop throgh incoming set of indices
  //Return index of minimum value
  int size = s.size();
  int minNum = INF;
  int minIndex = -1;
  for(int i=0; i< size; i++)
  {
    if(D[s.elementAt(i)] < minNum)
    { 
      minNum = D[s.elementAt(i)];
      minIndex = s.elementAt(i);
    }
  }
  return minIndex;
}
//Min of two ints
int min(int x,int y)
{
  if(x<y)
  {
    return x;
  }
  return y;
}

//Zero indexed printing function
void printUpdate()
{
  //Print contents of S
  int size = S.size();
  cout << "{";
  for(int i=0; i< size-1; i++)
  {
    cout << S.elementAt(i) <<",";
  }
  cout << S.elementAt(size-1) << "}";
  if(size >3)
  {
    cout << "\t";
  }
  else
  {
    cout << "\t\t";
  }
  
  cout << w << "\t";
  cout << D[1] << "\t" << P[1] << "\t";
  cout << D[2] << "\t" << P[2] << "\t";
  cout << D[3] << "\t" << P[3] << "\t";
  cout << D[4] << "\t" << P[4] << "\t";
  cout << D[5] << "\t" << P[5] << "\t";
  cout << endl;
}

//One indexed printing function
void printUpdateOneIndexed()
{
  //Print contents of S
  int size = S.size();
  cout << "{";
  for(int i=0; i< size-1; i++)
  {
    cout << S.elementAt(i)+1 <<",";
  }
  cout << S.elementAt(size-1)+1 << "}";
  if(size >3)
  {
    cout << "\t";
  }
  else
  {
    cout << "\t\t";
  }
  
  cout << w+1 << "\t";
  cout << D[1] << "\t" << P[1]+1 << "\t";
  cout << D[2] << "\t" << P[2]+1 << "\t";
  cout << D[3] << "\t" << P[3]+1 << "\t";
  cout << D[4] << "\t" << P[4]+1 << "\t";
  cout << D[5] << "\t" << P[5]+1 << "\t";
  cout << endl;
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
  
  //Do dikjstra procedure
  //Init D
  int i;
  D[0] = INF; //Cost from node to self (make inf so not used in path)
  P[0] = -1; //Start of shortest path - not node before
  for(i=1; i< NODES; i++)
  {
    D[i] = g.C[0][i];
    //Init P to be from starting node
    P[i] = 0;
  }
  
  //Print headers for results - zero or one indexed
  //cout << "ZERO INDEXED!" << endl;
  //cout << "S\t\t" << "w\t"<< "D[1]\t" << "P[1]\t"<< "D[2]\t" << "P[2]\t" << "D[3]\t" << "P[3]\t" << "D[4]\t" << "P[4]\t" << "D[5]\t" << "P[5]\t" << endl;
  cout << "ONE INDEXED!" << endl;
  cout << "S\t\t" << "w\t"<< "D[2]\t" << "P[2]\t"<< "D[3]\t" << "P[3]\t" << "D[4]\t" << "P[4]\t" << "D[5]\t" << "P[5]\t" << "D[6]\t" << "P[6]\t" << endl;
  
  //Print update with one indexed values - easier to check against book
  printUpdateOneIndexed();
  
  for(i=0; i < NODES-1; i++) //n-1 used in book
  {
    //choose a vertex w in V-S such that D[w] is a minimum;
    //V is set of all nodes so V-S is same as S_NOT
    Set vminuss = set_not(S);
    //Get index w of min
    w = minDNode(vminuss);
    //Add w to S
    S.add(w);
    //Recalculate v-s
    vminuss = set_not(S);
    int size = vminuss.size();
    int v;
    for(int j=0; j< size; j++)
    {
      v = vminuss.elementAt(j);//Get node from vminus
      //P-array can be updated here. If D[w]+C[w,v]<D[v] 
      //then we set P[v]:= w. -From book
      if( (D[w]+g.C[w][v])<D[v])
      {
	P[v] = w;
      }
      D[v] = min(D[v], D[w]+g.C[w][v]);      
    }
    //Print update with one indexed values - easier to check against book
    printUpdateOneIndexed();
  }
  return 0;
}