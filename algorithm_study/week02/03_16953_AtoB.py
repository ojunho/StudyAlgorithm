import sys
input = sys.stdin.readline

a, b = map(int, input().split())
res = 0
while b > a:
    if b%10 == 1:
        res += 1
        b = int(str(b)[:-1])
    elif b%2 == 1:
        break
    else:
        res += 1
        b = int(b/2)

if a != b:
    res = -1
else:
    res += 1

print(res)