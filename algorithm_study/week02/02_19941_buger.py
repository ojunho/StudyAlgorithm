import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(input().rstrip())

cnt = 0
for i in range(n):
    if arr[i] == 0:
        continue
    for j in range(k):
        if i+j+1 >= n:
            break
        if arr[i+j+1] == 0:
            continue
        if arr[i] != arr[i+j+1]:
            cnt += 1
            arr[i] = 0
            arr[i+j+1] = 0
            break

print(cnt)