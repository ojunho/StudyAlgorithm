import sys
input = sys.stdin.readline

n = int(input())
item = []

for _ in range(n):
    tmp_item = int(input())
    item.append(tmp_item)

item.sort(reverse= True)

for i in range(len(item)):
    if i%3 == 2:
        item[i] = 0

print(sum(item))