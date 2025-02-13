import sys

n_list = sys.stdin.readline().strip()

stack = []
temp = 1
result = 0
for i in range(len(n_list)):
    if n_list[i] == "(":
        stack.append(n_list[i])
        temp *= 2
    elif n_list[i] == "[":
        stack.append(n_list[i])
        temp *= 3
    elif n_list[i] == ")":
        if not stack or stack[-1] != "(":
            result = 0
            break
        if n_list[i - 1] == "(":
            result += temp
        temp //= 2
        stack.pop()
    else:
        if not stack or stack[-1] != "[":
            result = 0
            break
        if n_list[i - 1] == "[":
            result += temp

        temp //= 3
        stack.pop()
if stack:
    result = 0

print(result)
