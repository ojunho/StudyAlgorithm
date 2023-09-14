#include <stdio.h>
#include <iostream>
#define MAX_SIZE 1000

using namespace std;

void selectionSort(int a[], int n);

// 정렬이 제대로 되었는지 확인하기 위한 함수
void reprResult(int a[], int n){
    cout << "Sorted array: ";
    for(int i = 0; i < n; i++){
        cout << a[i] << " ";
    }
    cout << endl;
}

void swap(int* a, int* b){
    int tmp = *a;
    *a = *b;
    *b = tmp; 
}

int main(){
    int numTestCases;
    scanf("%d", &numTestCases);
    for (int i = 0; i < numTestCases; ++i){
        int num;
        int a[MAX_SIZE];
        scanf("%d", &num);
        for (int j = 0; j < num; j++){
            scanf("%d", &a[j]);
        }
        selectionSort(a, num);
        reprResult(a, num);
    }
    return 0; 
}


/* Selection Sort 함수 */
void selectionSort(int a[], int n){
    int countCmpOps = 0; // 비교 연산자 실행 횟수 
    int countSwaps = 0; // swap 함수 실행 횟수
    // selection sort 알고리즘 구현
    for(int i = 0; i < n-1; i++){
        int jMin = i;
        for(int j = i+1; j < n; j++){
            countCmpOps++;
            if(a[j] < a[jMin]){
                jMin = j;
            }
        }
        if(jMin != i){
            swap(&a[jMin], &a[i]);
            countSwaps++;
        }
    }
    printf("%d %d \n", countCmpOps, countSwaps);
}