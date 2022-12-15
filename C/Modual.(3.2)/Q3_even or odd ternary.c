#include<stdio.h>
int main()
{
   int n;
   char a,b,res;
   printf("Enter any number:");
   scanf("%d",&n);
   res=(n%2==0) ? 'a':'b';  

   printf("%c\n",res);
}