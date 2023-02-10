from collections import deque

n, w, L = map(int, input().split())
a_list = list(map(int, input().split()))
queue = deque([0 for _ in range(w)])
idx = 0
time = 0

while idx != n:
    queue.popleft()
    if sum(queue)+a_list[idx] <= L:
        queue.append(a_list[idx])
        idx += 1
    else:
        queue.append(0)
    time += 1

time += w
print(time)