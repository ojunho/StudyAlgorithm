# 두 수의 합
import sys
input = sys.stdin.readline

# 계수정렬
def sort(arr):
    ret = []
    count = [0] * (max(arr)+1)
    for i in range(len(arr)):
        count[arr[i]] += 1
    for i in range(len(count)):
        for j in range(count[i]):
            ret.append(i)
    return ret

def solve(arr, x):
    ret = 0
    min_i = 0
    max_i = len(arr)-1
    while True:
        # 맨처음과 맨끝에서 시작해서 점점 좁혀오다가 인덱스가 같아지거나 역전이 되면 멈춤.
        if not min_i < max_i:
            break
        elif arr[min_i] + arr[max_i] == x:
            ret += 1
            max_i -= 1
            min_i += 1
        elif arr[min_i] + arr[max_i] > x:
            max_i -= 1
        else:
            min_i += 1
    return ret

n = int(input())
arr = list(map(int, input().split()))
x = int(input())

s_arr = sort(arr)
res = solve(s_arr, x)
print(res)