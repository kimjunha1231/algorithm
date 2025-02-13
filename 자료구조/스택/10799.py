import sys

stack = []
n_list = sys.stdin.readline().strip()
count = 0


for i in range(len(n_list)):
    if n_list[i] == "(":
        stack.append(i)
    else:

        stack.pop()
        if n_list[i - 1] == "(":
            count += len(stack)
        else:
            count += 1

print(count)
