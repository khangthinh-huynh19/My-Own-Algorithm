#include <stdio.h>
#include <string.h>

int palindrome_check(int n, char arr[]){
    if (n % 2 == 0 ){
        for (int i = 0; i <= ((n/2) -1); i++){
            if (arr[i] != arr[n-i-1]){
                printf("Not a palindrome\n");
                break;
            }
            else if (i == (n/2) -1){
                printf("Palindrome\n");
            }
        }
    }
    else if (n%2 != 0){
        int mid_id = (n-1)/2;
        for (int i = 0; i <= mid_id-1;i++){
            if (arr[i] != arr[n-1-i]){
                printf("Not a palindrome\n");
                break;  
            }
            else if (i == mid_id-1){
                printf("Palindrome\n");
            }
        }
    }

}

int main(){
    while (1){ 
    char arr[100];
    printf("\nEnter a string: ");
    scanf("%s", arr);
    printf("Input string: %s\n", arr);
    int n = strlen(arr);
    printf("Size of the string: %d\n", n);
    palindrome_check(n, arr);
    }

    return 0;
}