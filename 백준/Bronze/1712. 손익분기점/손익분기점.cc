#include <stdio.h>

int main()
{
	int a; // 고정비용
	int b; // 가변비용
	int c; // 판매가격
	
	scanf("%d %d %d",&a,&b,&c);
	
	if(c>b)
		printf("%d\n",a/(c-b)+1);
	else
		printf("-1");

	return 0;
}