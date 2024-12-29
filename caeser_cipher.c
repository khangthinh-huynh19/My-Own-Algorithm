#include <stdio.h>
#include <string.h>
#include <stdlib.h>
void printArrayWithDots(char* arr, int size) {
    if (size < 1) {
        return;
    }

    for (int i = 0; i < size; i++) {
        if (i > 0) {
            printf(".");
        }
        printf("%d", arr[i]);
    }
}

int main(){
    char str[100];
    printf("Enter the string: \n");
    scanf("%s", str);
    printf("Input string: %s\n", str);
    int step;
    printf("Enter the step: \n");
    scanf("%d", &step);
    int n = strlen(str);
    printf("Length of string: %d", n);
    
    
    for (int i = 0; i < n; i++){
        if (str[i] >= 'a' && str[i]<='z'){
            int new_val = 'a' + (1 - (str[i] - 'a' + step)/26)*(str[i] - 'a' + step) + ((str[i] - 'a' + step)/26)*(str[i] - 'a' + step)%26;
            printf("\nNew ASCII value: %d", new_val);
            str[i] = new_val;
        }
    }

    printf("\nFormatted array: ");
    printArrayWithDots(str, n);
    printf("\n");
    return 0;
}