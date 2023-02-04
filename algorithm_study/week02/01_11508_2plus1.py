import sys
input = sys.stdin.readline

# 그리디 알고리즘이 생각이 안나서. 가장 싸게 하려면 할인을 많이 받아야됨.
# 할인 가장 많이 받으려면 세개씩 묶는 수가 가장 많아야함. 
# 비싼 금액을 할인 받으려면 정렬한 후에 비싼 순서대로 묶음. 세번째 값만 할인 받음.
n = int(input())
item = []

# 입력값들을 item 배열에 추가해서 
for _ in range(n):
    tmp_item = int(input())
    item.append(tmp_item)

# 정렬한다음
item.sort(reverse= True)

# 세번째 있는 항목들을 0으로 만든다음
for i in range(len(item)):
    if i%3 == 2:
        item[i] = 0

# 합한다.
print(sum(item))