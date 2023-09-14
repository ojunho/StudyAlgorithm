#include <stdio.h>
#include <iostream>
#define MAX_SIZE 1000

using namespace std;

void bubbleSort(int a[], int n);
void bubbleSortImproved1(int a[], int n);
void bubbleSortImproved2(int a[], int n);
void copyArray(int a[], int b[], int n);
void reprResult(int a[], int n);

int main(){

    int numTestCases;
    scanf("%d", &numTestCases);
    for (int i = 0; i < numTestCases; ++i){
        int num;
        int a[MAX_SIZE], b[MAX_SIZE];

        scanf("%d", &num);
        for (int j = 0; j < num; j++)
            scanf("%d", &b[j]);

        copyArray(a, b, num);
        bubbleSort(a, num);
        // reprResult(a, num);

        copyArray(a, b, num);
        bubbleSortImproved1(a, num);
        // reprResult(a, num);

        copyArray(a, b, num);
        bubbleSortImproved2(a, num);
        // reprResult(a, num);

        printf("\n");
    }
    return 0; 
}

void swap(int* a, int* b){
    int tmp = *a;
    *a = *b;
    *b = tmp; 
}

/* BubbleSort 함수 */
void bubbleSort(int a[], int n)
{
    int countCmpOps = 0; // 비교 연산자 실행 횟수 
    int countSwaps = 0; // swap 함수 실행 횟수
    // bubble sort 알고리즘 구현
    for(int pass = 1; pass < n; pass++){
        for(int i = 1; i <= n - pass; i++){
            countCmpOps++;
            if(a[i-1] > a[i]){
                countSwaps++;
                swap(&a[i-1], &a[i]);
            }
        }
    }
    printf("%d %d ", countCmpOps, countSwaps);
}

/* BubbleSort 함수 - Improved Version 1 */ 
void bubbleSortImproved1(int a[], int n){
    int countCmpOps = 0; // 비교 연산자 실행 횟수 
    int countSwaps = 0; // swap 함수 실행 횟수
    for(int pass = 1; pass < n; pass++){
        int swapped = false;
        for(int i = 1; i <= n - pass; i++){
            countCmpOps++;
            if(a[i-1] > a[i]){
                swap(&a[i-1], &a[i]);
                swapped = true;
                countSwaps++;
            }
            
        }
        if(swapped == false){
            break;
        }
    }
    printf("%d %d ", countCmpOps, countSwaps);
}

/* BubbleSort 함수 - Improved Version 2 */ 
void bubbleSortImproved2(int a[], int n){
    int countCmpOps = 0; // 비교 연산자 실행 횟수 
    int countSwaps = 0; // swap 함수 실행 횟수
    // bubble sort의 개선된 알고리즘 (2) 구현
    int lastSwappedPos = n;
    while(lastSwappedPos > 0){
        int swappedPos = 0;
        for(int i = 1; i < lastSwappedPos; i++){
            countCmpOps++;
            if(a[i-1] > a[i]){
                swap(&a[i-1], &a[i]);
                countSwaps++;
                swappedPos = i;
            }
        }
        lastSwappedPos = swappedPos;
    }
    printf("%d %d ", countCmpOps, countSwaps);
}

void copyArray(int a[], int b[], int n){
    for (int i = 0; i < n; i++){
        a[i] = b[i]; 
    }     
}

// 정렬이 제대로 되었는지 확인하기 위한 함수
void reprResult(int a[], int n){
    cout << "Sorted array: ";
    for(int i = 0; i < n; i++){
        cout << a[i] << " ";
    }
    cout << endl;
}