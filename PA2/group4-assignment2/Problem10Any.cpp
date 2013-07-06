/* Problem Description:

Fast Fourier Transform: any size

Compile and run with 
g++ Problem10Any.cpp -o Problem10Any && ./Problem10Any

Put all code in one file for easier submission
*/

#include <iostream>
#include <complex> //Complex numbers
#include <vector> //Easier to use than array in this case

using namespace std;

//Pi const
double pi = 3.14159265359;
//i constant value
complex<double> i = complex<double>(0,1); 

//Get is a number is prime
bool isPrime(int n)
{
  //Loop up to the sqrt(n)
  int upperbound = sqrt(n);
  
  for(int j =2; j <= upperbound; j++)
  {
    if( (n%j) ==0)
    {
      return false;
    }
  }
  return true;  
}

//Function for frequently used ξ
complex<double> xi(int n)
{
  //Beware of signs coming out of this
  //return values for special cases
  if(n==2) return complex<double>(-1,0);
  if(n==4) return i;
  
  return exp((2*pi/n)*i);
}

void getFactors(int n, int * r1, int *r2)
{
  //Quick dumb choice start with n/2 and decrement looking for factors
  int start = n/2;
  
  for(int j = start; j>0; j--)
  {
    if(n%j == 0)
    {
      //Found a factor
      *r1 = j;
      *r2 = n/j;
      cout << "Factors for " << n << ": " << *r1 << " " << *r2 << endl;
      return;
    }
  }
  cout << "Error: No factors for " << n << " found." << endl;  
}



//Returns vector of complex numbers
vector< complex<double> > FFT(int n, vector< complex<double> > x)
{
  //General error check
  if(x.size() == 0)
  {
    cout << "Error: x vector is uninitialized." << endl;
    //Return empty vector
    return vector< complex<double> >();
  }
  if(n == 0)
  {
    cout << "Error: FFT size is zero." << endl;
    //Return empty vector
    return vector< complex<double> >();
  }
  if(x.size() != n)
  {
    cout << "Error: x size and n are unequal." << endl;
    cout << "x.size()="<<x.size() << endl;
    cout << "n="<<n << endl;
    //Return empty vector
    return vector< complex<double> >();
  }
  
  //Main FFT calculation  
  //Return vector to populate
  vector< complex<double> > fft;
  //Initialize vector to size n
  int k;
  for(k=0; k < n; k++)
  {
    fft.push_back( complex<double>(0.0,0.0));
  }
  
  //Different procedures for prime or not
  int j;
  if(isPrime(n))
  {
    //Prime n
    for(j=0; j <n; j++)
    {
      //Calculate fft[j] with sum
      complex<double> sum = complex<double>(0.0,0.0);
      for(k=0; k< n; k++)
      {
	complex<double> toAdd = x[k]*pow(xi(n),j*k);
	//Something is messed up here with the sign of the imaginary component
	//Reverse it?
	toAdd = complex<double>(real(toAdd),-1*imag(toAdd));
	sum+= toAdd;
      }
      fft[j] = sum;
    }
    return fft;
  }
  else
  {
    //Composite n
    //Get factors
    int r1, r2;
    getFactors(n,&r1,&r2);
    //a is a vector of vectors, length r1
    vector< vector< complex<double> > > a;
    //Initialize a here rather than pushing back later
    //Easier to translate code from book
    for(k=0; k<r1; k++)
    {
      a.push_back(vector< complex<double> >());
    }
    
    int m; //Multiplier
    for(k=0; k<r1; k++)
    {
      //Populate array to pass into fft
      vector< complex<double> > newx;
      for(m=0; m<r2; m++)
      {
	//m goes 0,1,2...r2-1
	newx.push_back(x[k+m*r1]);
      }
      //Pass to fft and store results in a
      a[k]= FFT(r2,newx);
      //Error check, a[k] should have size r2
      if(a[k].size() != r2)
      {
	cout << "ak vector is not size r2." << endl;
      }
    }
    
    for(j=0; j<n; j++)
    {
      //Calculate fft[j] with sum
      complex<double> sum = complex<double>(0.0,0.0);
      for(k=0; k< r1; k++)
      {
	complex<double> toAdd = (a[k][j%r2])*pow(xi(n),k*j);
	//Something is messed up here with the sign of the imaginary component
	//Reverse it?
	toAdd = complex<double>(real(toAdd),-1*imag(toAdd));
	sum+= toAdd;
      } 
      fft[j] = sum;
    }
    return fft;
  }
}

int main()
{
  //Try fft on a sample data set
  //Let's try something simple like
  vector< complex<double> > testvals;
  int n = 6;
  cout << "Input data: ";
  int j;
  for(j=0; j<n; j++)
  {
    testvals.push_back(complex<double>(j,n-j));
    cout << testvals[j] << " ";
  }
  cout << endl;
  
  //Get fft of above (0,0) , (1,1)
  vector< complex<double> > fftresults = FFT(n,testvals);
  
  //Print results
  cout << "Results: ";
  for(j=0; j<n; j++)
  {
    cout << fftresults[j] << " ";
  }
  cout << endl;
  
  cout << "MATLab Results for x= [0 + 6i,1+5i,2+4i,3+3i,4+2i,5+1i] (n=6) " << endl;
  cout << "15.0000 +21.0000i ,  2.1962 + 8.1962i,  -1.2679 + 4.7321i , -3.0000 + 3.0000i, -4.7321 + 1.2679i , -8.1962 - 2.1962i";
  cout << endl;
  
  return 0;
}