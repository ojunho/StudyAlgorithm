# N 번째로 큰 수 
import sys, heapq
input = sys.stdin.readline

n = int(input())
hq = [] #우선순위 큐 사용
for i in range(n):
    numbers = list(map(int, input().split()))
    for number in numbers:
        if len(hq) < n:
            heapq.heappush(hq, number)
            continue
        if hq[0] >= number:
            continue
        
        heapq.heappop(hq)
        heapq.heappush(hq, number)
    
print(hq[0])