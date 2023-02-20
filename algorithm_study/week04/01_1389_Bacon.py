from collections import deque
import sys
input = sys.stdin.readline

def bfs(n, graph):
    res_list = []
    for i in range(1, n+1):
        dis_list = [0]*(n+1)
        distance = 0
        queue = deque([i])
        dis_list[i] = 1

        while queue:
            v = queue.popleft()
            distance = dis_list[v] + 1
            for j in graph[v]:
                if dis_list[j] == 0:
                    queue.append(j)
                    dis_list[j] = distance
        
        tmp_res = sum(dis_list)-1
        res_list.append(tmp_res)
    res = res_list.index(min(res_list)) + 1
    return res

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    tmp_list = list(map(int, input().split()))
    graph[tmp_list[0]].append(tmp_list[1])
    graph[tmp_list[1]].append(tmp_list[0])
for i in graph:
    i.sort()

res = bfs(N, graph)
print(res)