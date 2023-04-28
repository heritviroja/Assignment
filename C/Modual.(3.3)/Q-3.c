#include <stdio.h> 
#include <string.h> 

char* reverse(char *s, int a, int temp);

void main(void) 
{
    char s[20];
    printf("Enter a string: ");
    scanf("%s", &s);
    printf("Reverse: %s", reverse(s, strlen(s), 0));
} 
char* reverse(char *s,int a, int temp) 
{
    if (temp > (a - 1)) 
    { 
        return s;
    } 
    int c = s[temp]; 
    s[temp] = s[a - 1];
    s[a - 1] = c; 
    return reverse(s, (a - 1), (temp + 1)); 
}