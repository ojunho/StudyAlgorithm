from collections import deque
import sys
input = sys.stdin.readline

def bfs(g, s_x, s_y, e_x, e_y):
    queue = deque()
    queue.append((s_x, s_y))
    g[s_x][s_y] = 1 

    while queue:
        x, y = queue.popleft()
        if x == e_x and y == e_y:
            return g[e_x][e_y]-1

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < len(g) and 0 <= ny < len(g) and g[nx][ny] == 0:
                queue.append((nx, ny))
                g[nx][ny] = g[x][y] + 1

    return g[e_x][e_y]-1

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]
N = int(input())
# testCase loop
res_list = []
for i in range(N):
    map_size = int(input())
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    graph = [[0]*map_size for j in range(map_size)]
    res = bfs(graph, start_x, start_y, end_x, end_y)
    res_list.append(res)
for r in res_list:
    print(r)