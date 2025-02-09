import sys

N = int(sys.stdin.readline())
list = []
for i in range(N):
    list.append(int(sys.stdin.readline()))

print("\n".join(map(str, sorted(list, reverse=True))))
