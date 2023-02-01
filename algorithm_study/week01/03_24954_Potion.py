import sys
from itertools import permutations

N = int(sys.stdin.readline().rstrip())

# 원래 가격, 할인정보, 가능한 모든 case 순서, res는 가장 작은 값으로 향하도록 만드는데, 모두 할인 안받고 사는 가격으로 초기설정
og_price = list(map(int, sys.stdin.readline().split()))
sales_list = [[] for _ in range(N)]
cases_list = permutations(range(0,N), N) #num of cases
res = sum(og_price)

for i in range(N):
    tmp_num = int(sys.stdin.readline().rstrip())
    for j in range(tmp_num):
        tmp_sales = list(map(int, sys.stdin.readline().split()))
        sales_list[i].append(tmp_sales)


#
# #test
# for i in cases_list:
#     print(i)

for i in cases_list: # [0, 1, 2, 3]
    tmp_price = og_price[:]
    tmp_res = 0

    # ex) 1, 2, 3, 4, 번 물약을 순서대로 구매했을 때
    for j in i:
        tmp_res += tmp_price[j]
        for a, d in sales_list[j]: #a는 할인품목, d는 그 품목의 할인가격
            tmp_price[a-1] = max(1, tmp_price[a-1]-d) #할인받은 금액으로 구매(1원보다 작아질 수는 없기 때문에)

    # case 1개를 지났을 때 나오는 가격인 tmp_res가 현재 이전까지 계산된 가격중에 제일 싼 것보다도 싸면 그것을 채택
    res = min(res, tmp_res)

print(res)
