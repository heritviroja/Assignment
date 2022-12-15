#include<stdio.h>
int main()
{
	int a,b,sum,subtract,Multiply;
	float divide;
	
	printf("input any two number\n");
	scanf("%d""%d",&a,&b);
	sum=a+b;
	subtract=a-b;
	Multiply=a*b;
	divide=a/b;
	printf("%d\n",sum);
	printf("%d\n",subtract);
	printf("%d\n",Multiply);
	printf("%.2f\n",divide);
}