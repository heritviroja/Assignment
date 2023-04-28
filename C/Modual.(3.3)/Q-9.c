#include <stdio.h>

typedef struct 
    {
        int empno; 
        char empname[30]; 
        char address[100]; 
        int age;
    } 
    employee; 
    
void main (void)
{ 
    employee first;
    printf("Enter empoloyee Id: "); scanf("%d", &first.empno); 
    printf("Enter empoloyee Name: "); scanf("%s", &first.empname);
    fflush(stdin); 
    printf("Enter empoloyee address: "); 
    scanf("%[^\n]%*c", &first.address); 
    printf("Enter employee age: "); scanf("%d", &first.age);
}
