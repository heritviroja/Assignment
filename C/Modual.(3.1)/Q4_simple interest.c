#include<stdio.h>
int main()
{
	float p,a,r,t,A;
	printf("Input Principle amount:");
	scanf("%f",&p);
	printf("Input interst rate:");
	scanf("%f",&r);
	printf("Input time (in Year):");
	scanf("%f",&t);
	A = (p*r*t)/100;
	printf("Simple Interest in Rs.= %.2f",A);
}