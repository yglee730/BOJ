#include <stdio.h>
#include<math.h>

int main() 
{
	long long x,y;
	long long a;
	int n;
	
	scanf("%d",&n);
	
	for(int i=0; i<n; i++)
	{
		scanf("%lld %lld",&x,&y);
		
		a = (int)sqrt(y-x);
		
		if((a*a)==(y-x))
			printf("%lld\n",a*2-1);
		else if((a*a)<(y-x) && (y-x)<=(a*a)+a)
			printf("%lld\n",2*a);
		else if((a*a)+a<(y-x) && (y-x)<(a+1)*(a+1))
			printf("%lld\n",(2*a)+1);
	}

    return 0;
}
