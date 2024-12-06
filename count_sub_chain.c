#include <stdio.h>

int count_trend_sub_chain(int a[], int n, int len_chain){
    int n_ele_chain = 0;
    int n_chain = 0;
    for (int i = 0; i < n - 1; i++){
        if ((a[i+1] - a[i]) == 1){
            n_ele_chain += 1;
        }
        else if ((a[i+1] - a[i]) != 1)
        {
            if (n_ele_chain >= len_chain - 1){
                n_chain += 1;
                n_ele_chain = 0;
            }
            else
            {
                n_ele_chain = 0;
            }
        }
    }
    return n_chain;
}

int main(){
    int n, len_chain;
    int a[100];
    printf("Input the length of array: \n");
    scanf("%d", &n);
    printf("Input the lenght of sub chain: \n");
    scanf("%d", &len_chain);
    printf("Input the element of array: \n");
    for (int i = 0; i < n;i++){
        printf("Value %d \n", i);
        scanf("%d", &a[i]);
    }
    int n_chain = count_trend_sub_chain(a, n, len_chain);
    printf("Number of trend subchains is: %d", n_chain);
    return 0;
}