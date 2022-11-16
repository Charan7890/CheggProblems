
#include <iostream>

using namespace std;

// global declared variables.
int arr[100000];
int i=0;

// Fibonacci Series code using recursion.
//example :- 0,1,1,2,3,5,8,13....
// fib(5) = 5.
int Fib(int n){
    if(n==0||n==1){
        return n;
    }
    else{
        return(Fib(n-1)+Fib(n-2));
    }
}

// recFib(start,end) function.
void recFib(int start,int end){
        if(start>end){
        return;
    }
    else{
        arr[i++]=Fib(start);
        recFib(start+1,end);
    }
}



int main()
{
    
    //0-based fibonacci series.
    //Part - 1:
    cout<<"***********Part-1:scenario***********"<<endl;
    cout<<"Enter a number(0-based indexed) to find fibonacci at that position:\n";
    
    // declaring n variable.
    int n;
    
    // taking input for n variable.
    cin>>n;
    
    // calling recursive function to get the answer at particular position. This function returns int type
    // value which will be stored in result variable.
    int result = Fib(n);
    
    cout<<result<<endl;
    
    // to seperate the two cases it is drawn.
    cout<<"----------------------------------------------------------------------"<<endl;;
    
    //code for part-2 type recursion.
    cout<<"*****Part-2:scenario developed using the part-1 recursion*****"<<endl;
    cout<<"Enter start and end point of fibonacci(inclusive)[0-based indexed]:\n";
    // declaring start and end variables.
    int start,end;
    
    // taking input for start and end variables from the user.
    cin>>start>>end;
    
    // calling recursion function named recFib().
    recFib(start,end);
    
    // to print the values of a global array.
    for(int i=0;i<end-start+1;i++){
        cout<<arr[i]<<" ";
    }
    // For moving cursor to the next line.
    cout<<endl;

    return 0;
}
