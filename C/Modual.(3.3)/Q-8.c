char s[20];
char c[20]; 
int palindrome = true;
printf("Enter a string: ");
scanf("%s", &s);

int length = strlen(s); 

for (int i = length; i > 0; i--)
{ 
    c[i - 1] = s[length - i]; 
} 

printf("Reverse: %s\n" c); 

for (int i = 0; i < length; i++) 
{ 
    if (s[i] != c[i]) 
    {
        palindrome = false;break;
    } 
} 
