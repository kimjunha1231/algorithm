import sys

stack = []
n_list = sys.stdin.readline().strip()
count = 0
for i in n_list:
    if i == "(":
        count += 1
        stack.append(i)
    else:
        count += 1
        stack.pop()
print(count)
