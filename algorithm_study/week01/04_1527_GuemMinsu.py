import sys
from itertools import product

res = 0
res_list = []
iter_list = [4, 7]
range_min, range_max = map(int, sys.stdin.readline().split())

# iterator 로 수를 생성할때 자릿수에 맞춰서 조금만 생성하려고
# if 입력이 1, 10 이라고 한다면 4, 7, 44,,, 77까지만 만들기 위해서. 만약 range_max로 만들게 되면 7777777777 까지 만들게 된다.
len_min = len(str(range_min))
len_max = len(str(range_max))

for i in range(len_min, len_max+1):
    tmp_list = list(product(iter_list, repeat=i))
    for j in tmp_list:
        res_int = int(''.join(map(str, j)))
        res_list.append(res_int)

for i in res_list:
    if range_min <= i <= range_max:
        res += 1

print(res)