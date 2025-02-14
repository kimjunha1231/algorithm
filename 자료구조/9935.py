import sys

sys.setrecursionlimit(1000000)


char_list = sys.stdin.readline().strip()
boom = sys.stdin.readline().strip()
stack = []


for i in char_list:
    stack.append(i)
    if "".join(stack[-len(boom) :]) == boom:
        del stack[-len(boom) :]

if stack:
    print("".join(stack))
else:
    sys.stdout.write("FRULA")
