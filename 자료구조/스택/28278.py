import sys

N = int(sys.stdin.readline())

stack = []
for i in range(N):
    num_list = list(map(int, sys.stdin.readline().split()))
    if num_list[0] == 1:
        stack.append(num_list[1])
    elif num_list[0] == 2:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif num_list[0] == 3:
        print(len(stack))
    elif num_list[0] == 4:
        if stack:
            print(0)
        else:

            print(1)
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)
