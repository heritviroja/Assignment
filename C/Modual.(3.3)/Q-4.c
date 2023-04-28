#include <stdio.h>
int factorial(int a);

void main (void)
{ 
    int a;
    printf("Enter a number: ");
    scanf("%d", &a);
    printf("Factorial: %d", factorial(a));
} 
int factorial(int a) 
{ 
    int fact;
    if(a == 1)
    { 
        return; 
    } 
    fact = a * factorial(a - 1); 
    return fact; 
} 
