
#include <stdio.h>
#include<string.h>

int main()
{
    // to store char array of size - 10.
    char a[11];
    
    // key variable is used to store character value, which the user want to search.
    char key;
    
    int i,flag;
    
    // taking input from user
    printf("Enter any 10 letters:\n");
    scanf("%s",a);
    
    // taking character input from the user to search in the string.
    printf("Enter a character you want to search:\n");
  
  // NOTE: generally, scanf treats enter key as a special key, that's why we are not able to take another input.
  // getchar() function will delete the enter key for the previous scanf function, that's how it helps in taking another character input.
    getchar();
    scanf("%c",&key);
    
    
    // flag variable is used to encounter whether the element found or not.
    i=0,flag=0;
    // below code is used to match the Character in the given string.
    while(a[i]!='\0'){
        
        if(a[i]==key){
            flag=1;
            break;
        }
        i+=1;

    }
    
    if(flag==1){
        printf("Character found at position:%d",i);
    }
    else{
        printf("Character is not present.");
    }

    return 0;
}
