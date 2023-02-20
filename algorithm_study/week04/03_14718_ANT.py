from collections import deque
import sys
input = sys.stdin.readline

def printg(g):
    for i in range(len(g)):
        for j in g[i]:
            print(j, end=" ")
        print()

def bfs(y, x):
    queue = deque()
    queue.append((y, x))
    graph[y][x] = 0
    while queue:
        y, x = queue.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph[ny][nx] == 1:
                queue.append((ny, nx))
                graph[ny][nx] = 0

dx = [1, 1, 1, 0, -1, -1, -1, 0]
dy = [1, 0, -1, -1, -1, 0, 1, 1]

# making graph
graph = []
M, N = map(int, input().split())
for _ in range(M):
    tmp_list = list(map(int, input().split()))
    graph.append(tmp_list)

cnt = 0
for i in range(M):
    for j in range(N):
        if graph[i][j] == 1:
            bfs(i, j)
            cnt += 1
print(cnt)