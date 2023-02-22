# 좌표 압축
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
x_arr = arr[:]
arr = sorted(list(set(arr)))
dic = {arr[i] : i for i in range(len(arr))}
res = []
for i in x_arr:
    res.append(dic[i])
print(*res)