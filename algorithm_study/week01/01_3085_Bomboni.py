import sys
input = sys.stdin.readline

def check(lst):
    res = 1
    for i in range(len(lst)):

        # 가로로 같은 색이 연달아서 나오는 경우 확인
        cnt = 1
        for j in range(1, len(lst)):
            if lst[i][j] == lst[i][j-1]:
                cnt += 1
                res = max(cnt, res)
            else:
                cnt = 1

        # 세로로 같은 색이 연달아서 나오는 경우 확인.
        cnt = 1
        for j in range(1, len(lst)):
            if lst[j][i] == lst[j-1][i]:
                cnt += 1
                res = max(cnt, res)
            else:
                cnt = 1
    return res

n = int(input())
og_list = [list(input().rstrip()) for _ in range(n)]
res = 0

for i in range(n):

    for j in range(n):
        if j+1 < n: # 인덱싱 잡아주기

            # 가로로 바꿔주고 check() 함수 사용해서 몇개인지 확인하고
            og_list[i][j], og_list[i][j+1] = og_list[i][j+1], og_list[i][j]
            tmp_res = check(og_list)

            #가장 큰 값을 res 값으로.
            if tmp_res > res:
                res = tmp_res

            #다시 원래대로 바꿔주고
            og_list[i][j], og_list[i][j+1] = og_list[i][j+1], og_list[i][j]

        if i+1 < n:

            # 세로 방향으로 바꿔주고, check() 함수 사용해서 몇개인지 확인하고
            og_list[i][j], og_list[i+1][j] = og_list[i+1][j], og_list[i][j]
            tmp_res = check(og_list)

            # 더 큰값을 res가 받도록 한다.
            if tmp_res > res:
                res = tmp_res

            # 다시 원래대로 돌려주ㅌ
            og_list[i][j], og_list[i+1][j] = og_list[i+1][j], og_list[i][j]
print(res)