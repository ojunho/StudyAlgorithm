test_str = input()
stack = []
res = 0
for i in range(len(test_str)):
    if test_str[i] == '(':
        stack.append(test_str[i])
        res += 1
    elif test_str[i] == ')':
        if test_str[i-1] == '(':
            stack.pop()
            res += len(stack)
            res -= 1
        else:
            stack.pop()
print(res)
    

