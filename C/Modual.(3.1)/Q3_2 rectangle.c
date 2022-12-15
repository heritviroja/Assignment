#include<stdio.h>
int main()
{
	float h,b,A;
	printf("Input height of Triangle:");
	scanf("%f",&h);
	printf("Input base of Triangle:");
	scanf("%f",&b);
	A=(h*b)/2;
	printf("Area of Triangle= %.2f",A);
}