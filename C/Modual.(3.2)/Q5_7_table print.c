#include<stdio.h>
int main()
{
  int x,number;
  printf("Enter any number:");
  scanf("%d",&number);
  for(x=1;x<=10;x++)
{
printf("%d * %d = %d\n", number,x,x*number);
}
}
