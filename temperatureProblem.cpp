#include <iostream>

using namespace std;

int inspectTemp(double temps[],int size){
    int count = 0;
    for(int i=0;i<size;i++){
        if(temps[i]>=28 && temps[i]<=32){
            // do nothing
        }
        else{
            count=count+1;
        }
    }
    return count;
}
int main()
{
    int num_of_days;
    cout<<"Enter number of days:";
    cin>>num_of_days;
    int num_of_readings;
    num_of_readings = num_of_days*2;
    
    double *temps= new double[num_of_readings];
    
    for(int i=0;i<num_of_readings;i++){
        double temp;
        cout<<"Please enter the temperature in F for reading "<<(i+1)<<" :";
        cin>>temp;
        temps[i] = temp;
    }
    
    int count = inspectTemp(temps,num_of_readings);
    
    if(count>2){
        cout<<"error: count is outside the safe range";
    }
    else{
        cout<<"Temperature was well within the normal range:\nA yummy dish coming right up";
    }
    
    delete[] temps;
    
    return 0;
}
