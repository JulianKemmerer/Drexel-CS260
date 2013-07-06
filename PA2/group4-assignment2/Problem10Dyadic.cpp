/* Problem Description:

Fast Fourier Transform: dyadic size

Compile and run with 
g++ Problem10Dyadic.cpp -o Problem10Dyadic && ./Problem10Dyadic

Put all code in one file for easier submission
*/

#include <iostream>
#include <complex> //Complex numbers
#include <vector> //Easier to use than array in this case

using namespace std;


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
  
  //End condition
  if(n==1)
  {
    fft[0] = x[0];
    return fft;
  }
  else
  {
    vector< complex<double> > evenarray;
    vector< complex<double> > oddarray;
    //Populate both arrays
    for(k=0; k<=(n-2); k+=2)
    {
      //even: k goes 0,2,4...n-2
      //odd: k+1 goes 1,3,5...n-1
      evenarray.push_back(x[k]);
      oddarray.push_back(x[k+1]);
    }
    
    //Error check
    //u and v should be size n/2
    if( (evenarray.size() != (n/2)) || (oddarray.size() != (n/2)))
    {
      cout << "Error: even and odd array not size n/2." << endl;
      //Return empty vector
      return vector< complex<double> >();
    }
    
    //Compute u and v arrays
    vector< complex<double> > u;
    vector< complex<double> > v;
    u=FFT(n/2,evenarray);
    v=FFT(n/2,oddarray);
    
    int j;
    complex<double> i = complex<double>(0,1); //i constant value
    complex<double> tau;
    double pi = 3.14159265359;
    complex<double> exparg;
    for(j=0; j< n; j++)
    {
      //Need to seperate out to work with overloaded complex library functions
      exparg = ((2*pi*j)/n) * i;
      tau = exp(exparg);
      fft[j]=u[j%(n/2)] + tau*v[j%(n/2)];
    }
    return fft;
  }
}

int main()
{
  //Try fft on a sample data set
  //Let's try something simple like
  vector< complex<double> > testvals;
  int n = 8;
  cout << "Input data: ";
  for(int i=0; i<n; i++)
  {
    testvals.push_back(complex<double>(i,0));
    cout << testvals[i] << " ";
  }
  cout << endl;
  
  //Get fft of above 0,1,2,3,4,5.. (no complex values)
  vector< complex<double> > fftresults = FFT(n,testvals);
  
  //Print results
  cout << "Results: ";
  for(int i=0; i<n; i++)
  {
    cout << fftresults[i] << " ";
  }
  cout << endl;
  
  cout << "MATLab Results (n=8): " << endl;
  cout << "28.0000 + 0i   -4.0000 + 9.6569i  -4.0000 + 4.0000i  -4.0000 + 1.6569i   -4.0000 + 0i   -4.0000 - 1.6569i  -4.0000 - 4.0000i  -4.0000 - 9.6569i" << endl;
  
  
  return 0;
}