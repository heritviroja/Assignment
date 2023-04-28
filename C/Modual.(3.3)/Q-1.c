void main(void)
{
int a[10]; 
for (int i = 0; i < 10; i++) { 
    scanf("%d", &a[i]); 
} 
    printf("Max number: %d", max_bata(a, 10)); 

} 
int max_bata(int a[], int Length)
{ 
    int max = a[0];
    for (int i = 1; i < Length; i++) 
    { 
        if (max < a[i])
        { 
        max = a[i]; 
        }
    } 
 
return max; 
}