#include <stdio.h> 
void main(void)
{
    char *s; 
    printf("Enter a string: ");
    scanf("%s", s); 
    int i =0; 
    while (s[i] != '\0') 
    { 
        i++; 
    }
    printf("Length: %d", i); 

} 

