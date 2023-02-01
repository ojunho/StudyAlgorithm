import sys

N, M = map(int, sys.stdin.readline().split())

N_set = set()
res = 0

#N 만큼의 단어를 집합에 넣어주고
for _ in range(N):
    tmp_str = sys.stdin.readline().rstrip()
    N_set.add(tmp_str)

# test_ string을 한줄씩 받으면서 set에 있으면 res 값을 1씩 증가시킨다.ㅌ
for _ in range(M):
    test_str = sys.stdin.readline().rstrip()
    if test_str in N_set:
        res += 1

print(res)