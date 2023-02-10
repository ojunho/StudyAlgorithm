# from itertools import combinations
# import sys
# input = sys.stdin.readline

# while True:
#     caseL = list(map(int, input().split()))
#     n = caseL[0]
#     if n == 0:
#         break
#     caseL = caseL[1:]
#     comb = list(combinations(caseL, 6))
#     for c in comb:
#         for i in c:
#             print(i, end=" ")
#         print()
#     print()

def dfs(depth, idx):
    if depth == 6:
        for i in out:
            print(i, end=" ")
        print()
        return
    
    for i in range(idx, n):
        out.append(caseL[i])
        dfs(depth+1, i+1)
        out.pop()

while True:
    caseL = list(map(int, input().split()))
    n = caseL[0]
    if n == 0:
        break
    caseL = caseL[1:]
    out = []
    dfs(0, 0)
    print()

