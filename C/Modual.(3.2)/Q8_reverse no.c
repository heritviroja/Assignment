#include<stdio.h>
int main()
{
    int number=64728,rem,res=0;
    while (number!=0)
    {
        rem=number%10;
        res=res*10+rem;
        number=number/10;
    }
    printf("%d",res);
    return 0;
}