
#include <bits/stdc++.h>
#include<algorithm>

using namespace std;
vector<string> players;

void addAPlayer(){
    string name;
    cout<<"Enter a player name to add:";
    cin>>name;
    players.push_back(name);
    cout<<"Player added successfully"<<endl;
    
}

int removeAPlayer(){
    string remove_name;
    cout<<"enter a player name to remove:";
    cin>>remove_name;
    int index = -1;
    for(int i=0;i<players.size();i++){
        if(remove_name==players.at(i)){
            index = i;
        }
    }
    players.erase( players.begin() + index );
    return index;
    
}

int searchAPlayer(){
    string search_name;
    int index = -1;
    cout<<"enter a player name to search:";
    cin>>search_name;
    for(int i=0;i<players.size();i++){
        if(search_name==players.at(i)){
            index = i;
        }
    }
    
    return index;
}

void sortPlayersByName(){
    if(players.size()==0){
        cout<<"There are no players in the team to sort by name."<<endl;
    }
    else{
        sort(players.begin(),players.end());
        cout<<"Players successfully sorted by name."<<endl;
    }
    
}

void displayPlayers(){
    for (int i = 0; i < players.size(); i++)
        cout << players[i] << " ";
    cout<<endl;
}

int main()
{
    cout<<"-------------------- Team USA --------------------"<<endl;
    while(true){
    cout<<"1.Add a player\n2.Remove a player\n3.Search a player\n4.Sort players by name\n5.Display players\n0.exit"<<endl;
    cout<<"--------------------------------------------------"<<endl;
    int option;
    cin>>option;
    if(option==1){
        addAPlayer();
    }
    else if(option==2){
       int index = removeAPlayer();
       if(index==-1){
           cout<<"There are no players in the team to remove."<<endl;
       }
    }
    else if(option==3){
        int index=searchAPlayer();
        if(index==-1){
            cout<<"Player not found."<<endl;
        }
        else{
            cout<<"player found"<<endl;
        }
    }
    else if(option == 4){
         sortPlayersByName();
    }
    else if(option==5){
        displayPlayers();
    }
    else if(option==0){
        break;
    }
    else{
        cout<<"Incorrect operator"<<endl;
    }
    }

    return 0;
}
