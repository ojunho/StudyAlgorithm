# 30의 배수
# 양수 N을 입력받아 그 수의 숫자를 조정해서 30의 배수가 되도록 한다.
# 30의 배수는 3의 배수이며 10의배수이다. 3의 배수는 자릿수의 합이 3의 배수이면 된다.
def sort(arr):
    res = ""
    count = [0] * (max(arr)+1)
    for i in range(len(arr)):
        count[arr[i]] += 1
    for i in range(len(count)-1, -1, -1):
        for j in range(count[i]):
            res += str(i)
    return res

# 30의 배수가 되지 않는 경우 판별
arr = list(map(int, input()))
if sum(arr) % 3 != 0 or 0 not in arr:
    print(-1)
    exit()

# 가장 큰수이기 때문에 정렬만 하면 된다. 0~9까지의 수로 한정되어있어 계수정렬로 품.
res = sort(arr)
print(res)