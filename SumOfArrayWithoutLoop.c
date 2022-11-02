

#include <stdio.h>

int recursiveSum(int *a,int n){
    int ans = 0;
    if(n<0){
        return 0;
    }
    else{
        return a[n-1]+recursiveSum(a,n-1);
    }
}

int main()
{
    int n;
    scanf("%d",&n);
    
    int a[1000000];
    for(int i=0;i<n;i++){
        scanf("%d",&a[i]);
    }
    int answer = recursiveSum(a,n);
    printf("The sum is:%d",answer);

    return 0;
}
