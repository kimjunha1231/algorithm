import sys


N = int(sys.stdin.readline())

top_list = list(map(int, sys.stdin.readline().split()))
result = []
stack = []

for i in range(N):
    while stack:
        if stack[-1][0] < top_list[i]:
            stack.pop()

        else:
            result.append(stack[-1][1] + 1)

            break
    if not stack:
        result.append(0)
    stack.append([top_list[i], i])
print(" ".join(map(str, result)))
