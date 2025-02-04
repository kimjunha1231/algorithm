import sys

N = int(sys.stdin.readline())


result = 0
n_list = []


if N != 0:
    for i in range(N):
        n_list = sys.stdin.readline().strip()
        stack = []
        for j in n_list:
            if j not in stack:
                stack.append(j)

            elif j in stack:
                if stack[-1] == j:
                    stack.pop()
                else:
                    stack.append(j)

        if len(stack) == 0:
            result += 1
print(result)
