#include<stdio.h>
int main()
{
   int i,j,space;
   for(i=1;i<=10;i++)
   {
   	for(space=1;space<=10-i;space++)
   	{
   		printf(" ");
	}
   	for(j=1;j<=i;j++)
   	{
   		if(i%2!=0)
   		{
   			printf("* ");
		}
	}
	printf("\n");
   }	
 
}




