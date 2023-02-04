import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(input().rstrip())

#배열 돌면서 k만큼 더 탐색한다음 현재 i 와 다른 j 가 있다면 둘다 0으로 바꿔버림. 결과값 +1
cnt = 0
for i in range(n):
    if arr[i] == 0:
        continue
    
    for j in range(k):

        # 인덱싱 넘어가는거 방지
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