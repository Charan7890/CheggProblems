
#include <iostream>

using namespace std;

int main()
{
    int n;
    //Taking input for numer of persons
    cout<<"enter number of persons:";
    cin>>n;
    string person;
    for(int i=0;i<n;i++){
        // taking binary number as input in string format
        cout<<"enter person-"<<i+1<<" binary number:";
        cin>>person;
        int count=0;
        int len = person.length();
        for(int j=0;j<len;j++){
            if(person[j]=='1'){
                count++;
            }
        }
        cout<<"Person-"<<i+1<<" encounters 1 for "<<count<<" times."<<endl;
    }

    return 0;
}
