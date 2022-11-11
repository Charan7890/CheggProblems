
#include <iostream>

using namespace std;

void swapElements(int arr[],int n){
    // cout<<"swap called"<<endl;
    
    // For even condition
    if(n%2==0){
        for(int i=0;i<n-1;i+=2){
            int temp = arr[i];  // temp variable is used to store value for temporary purpose.
            arr[i] = arr[i+1];
            arr[i+1] = temp;
        }
    }
    
    // For odd condition
    else{
        
        for(int i=0;i<n/2;i++){
            int temp = arr[i];   // temp variable is used to store value for temporary purpose.
            arr[i] = arr[n-i-1];
            arr[n-i-1] = temp;
            
        }
        
    }
}

int main()
{
    int n;
    // taking size input from user.
    cin>>n;
    
    // create new array dynamically using keyword new.
    int *arr = new int[n];
    
    // taking n inputs from the user and inserting into the array name 'arr'
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    
    // calling swapElements function.
    swapElements(arr,n);
    
    // displaying array elements.
    for(int i=0;i<n;i++){
        cout<<arr[i]<<" ";
    }

    return 0;
}
