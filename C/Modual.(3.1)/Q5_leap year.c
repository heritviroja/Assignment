#include<stdio.h>
int main()
{
    int y;
    printf("enter a Year :");
    scanf("%d",&y);
    if (y%4==0)
    {
        printf("Leap Year");
    }
    else
        printf("Non Leap Year");
    
}