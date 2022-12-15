#include<stdio.h>
int main()
{
    int i,j,x,y;
    for(i=1;i<=5;i++)
    {
        if(i%2==0)
        { 
            x=0;
            y=1;
        }
        else
        {
            x=0;
            y=1;											;
        }
        for(j=1;j<=i;j++)
        if(j%2!=0)
        {
		  printf("%d",y);
        }
		else
		{
			printf("%d",x);
		}
        printf("\n");
   		}
    }
