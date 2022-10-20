
#include <stdio.h>

int main()
{
    int T;  // to run test cases
    
    int K,N,M; 
    
/*  variables:
    K - "The number of packs atleast needed to fix the sink"
    N - "The number of packs Lilli has at home"
    M - "The number of packs left at Store"
*/

    int var=0; // to print test case numbers

    scanf("%d",&T);  // taking input for T.
    
    
    
    while(T>0) {  // running test cases
    
    var++;
    
    scanf("%d %d %d",&K,&N,&M);  // taking input for K,N and M.
    
     /* Evaluating the condition.
       i.e., The number of packs Lilli has at home(N) + The number of packs Lilli can buy from Store(M)
       
       should need to be equal or greater than K(The number of packs atleast needed to fix the sink)
       
       or else the sink can't be fixed.
       
    */
    
    if((N+M)>=K){
        printf("Case #%d :yes\n",var);
    }
    else{
        printf("Case #%d :no\n",var);
    }
    T--; 
    }
    return 0;
}
