from collections import deque
import sys
input = sys.stdin.readline

# PrintingGraph Def
def printg(g):
    print('*'*10)
    for i in range(len(g)):
        for j in range(len(g[0])):
            for k in g[i][j]:
                print(k, end=" ")
            print()
        print()
    print('*'*10)

# BFS Def
def bfs():
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if graph[i][j][k] == 1:
                    q.append((k, j, i))
    
    while q:
        x, y, z = q.popleft()
        for i in range(6):
            nx = x + d[i][0]
            ny = y + d[i][1]
            nz = z + d[i][2]
            if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H and graph[nz][ny][nx] == 0:
                q.append((nx, ny, nz))
                graph[nz][ny][nx] = graph[z][y][x] + 1
    
    ret = -1
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if graph[i][j][k] == 0:
                    return -1
                ret = max(ret, graph[i][j][k])
    return ret-1


M, N, H = map(int, input().split())
d = [
    (1, 0, 0),
    (0, -1, 0),
    (0, 0, 1),
    (-1, 0, 0),
    (0, 1, 0),
    (0, 0, -1)
]
q = deque()

#1 making graph 
graph = []
flag = 0
for i in range(H):
    tmp_graph = []
    for j in range(N):
        tmp_list = list(map(int,input().split()))
        if 0 in tmp_list:
            flag = 1
        tmp_graph.append(tmp_list)
    graph.append(tmp_graph)
if flag == 0:
    print(0)
    exit()
# printg(graph)

res = bfs()
print(res)