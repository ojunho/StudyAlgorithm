#include <stdio.h>
#include <iostream>
#include <cmath>
#define MAX_SIZE 1000

using namespace std;

void combSort(int a[], int n);
void reprResult(int a[], int n);

int main(){
    int numTestCases;
    scanf("%d", &numTestCases);
    for (int i = 0; i < numTestCases; ++i)
    {
        int num;
        int a[MAX_SIZE];
        scanf("%d", &num);
        for (int j = 0; j < num; j++){
            scanf("%d", &a[j]);
        }
        combSort(a, num);
        reprResult(a, num);
    }
    return 0; 
}

void swap(int* a, int* b){
    int tmp = *a;
    *a = *b;
    *b = tmp; 
}

// 정렬이 제대로 되었는지 확인하기 위한 함수
void reprResult(int a[], int n){
    cout << "Sorted array: ";
    for(int i = 0; i < n; i++){
        cout << a[i] << " ";
    }
    cout << endl;
}

/* comb sort 함수 */
void combSort(int a[], int n){
    int countCmpOps = 0; // 비교 연산자 실행 횟수 
    int countSwaps = 0; // swap 함수 실행 횟수
    // comb sort 알고리즘 구현
    int gap = n;
    float shrink = 1.3;
    bool sorted = false;

    while(sorted == false){
        gap = floor(gap / shrink);
        if(gap <= 1){
            gap = 1;
            sorted = true;
        }

        int i = 0;
        while(i + gap < n){
            countCmpOps++;
            if(a[i] > a[i+gap]){
                swap(&a[i], &a[i+gap]);
                countSwaps++;
                sorted = false;
            }
            i++;
        }
    }
    printf("%d %d \n", countCmpOps, countSwaps);
}