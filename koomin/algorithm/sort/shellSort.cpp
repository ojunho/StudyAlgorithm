#include <stdio.h>
#define MAX_SIZE 1000
#include <iostream>

using namespace std;

void ShellSort(int a[], int n);

// 정렬이 제대로 되었는지 확인하기 위한 함수
void reprResult(int a[], int n){
    cout << "Sorted array: ";
    for(int i = 0; i < n; i++){
        cout << a[i] << " ";
    }
    cout << endl;
}

int main(){
    int numTestCases;
    scanf("%d", &numTestCases);
    for (int i = 0; i < numTestCases; ++i)
    {
        int num;
        int a[MAX_SIZE];
        scanf("%d", &num);
        for (int j = 0; j < num; j++)
            scanf("%d", &a[j]);
        ShellSort(a, num);

        // 정렬 결과 확인 코드
        reprResult(a, num);
    }
    return 0;
}

void swap(int *a, int *b)
{
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

/* Shell Sort 함수 */
void ShellSort(int a[], int n)
{
    int countCmpOps = 0; // 비교 연산자 실행 횟수 
    int countSwaps = 0; // swap 함수 실행 횟수


    // Shell sort 알고리즘 구현
    int shrinkRatio = 2;
    int gap = n / shrinkRatio;

    while(gap > 0){
        for(int i = gap; i < n; i++){
            int tmp = a[i];
            int j = i;
            while(j >= gap){
                countCmpOps++;
                if(a[j-gap] > tmp){
                    a[j] = a[j-gap];
                    countSwaps++;
                }
                else{
                    break;
                }
                j -= gap;
            }
            a[j] = tmp;
        }
        gap /= shrinkRatio;
    }

    printf("%d %d \n", countCmpOps, countSwaps);
}