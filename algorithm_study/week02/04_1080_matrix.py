import sys
input = sys.stdin.readline

# 배열 arr, 인덱스(a,b)를 입력받아서 a,b 위치에서부터 3X3 만큼 다 뒤집어주는함수.
def change(arr, a, b): 
    for i in range(3):
        for j in range(3):
            if arr[a+i][b+j] == 0:
                arr[a+i][b+j] = 1
            else:
                arr[a+i][b+j] = 0
    return arr

n, m = map(int, input().split())
res = 0
game_changer = 0

a_list = []
b_list = []
for _ in range(n):
    tmp_a = list(map(int, input().rstrip()))
    a_list.append(tmp_a)
for _ in range(n):
    tmp_b = list(map(int, input().rstrip()))
    b_list.append(tmp_b)

for i in range(n):
    if game_changer == 1:
        break
    for j in range(m):
        if a_list[i][j] != b_list[i][j]:
            if i+2 >= n or j+2 >= m:
                game_changer = 1
                break
            a_list = change(a_list, i, j)
            res += 1
            # print(f"i:{i}, j:{j},, a_list=\n{a_list}")

if game_changer == 1:
    res = -1

print(res)