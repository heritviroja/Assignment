#include<stdio.h>
int main()
{
    int choice;
    char ch;
    printf("Enter any character:");
    scanf("%c",&ch);
    printf("Enter any choice:");
    scanf("%d",&choice);
    switch(choice)
   {
    case 1:
           if ((ch=='a' || ch=='e' || ch=='i' || ch=='o' || ch=='u' ||
	
	            ch=='A' || ch=='E' || ch=='I' || ch=='O' || ch=='U')) 
	      {
		     printf("Vowels");
	      }
	         else
	      {
				 printf("Consonants");

	      }
           break;
    
    default:
           printf("Invalid choice");
    }
    return 0;
}