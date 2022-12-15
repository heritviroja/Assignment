#include<stdio.h>
int main()
{
    int a,b;
    printf("input number 1:");
    scanf("%d",&a);
    printf("input number 2:");
    scanf("%d",&b);
    a=a+b; //12+23=35
    b=a-b; //35-23=12
    a=a-b; //35-12=23
    printf("a=%d\nb=%d\n",a,b);
}