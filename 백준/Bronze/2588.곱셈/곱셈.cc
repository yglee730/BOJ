#include <stdio.h>
 
int main()
{
 	int A,B;
 	
 	scanf("%d",&A);
 	scanf("%d",&B);
 	
 	int out_1 = A*(B%10);
 	
 	printf("%d\n",out_1);
 	
	B = B/10;
 	int out_2 = A*(B%10);
 	
 	printf("%d\n",out_2);
 	
 	B = B/10;
 	int out_3 = A*B;
 	
 	printf("%d\n",out_3);
	
	printf("%d",out_1 + (out_2*10)+ (out_3)*100);
	    
    return 0;
}