import sys

s = int(sys.stdin.readline())

a_list = sorted(list(map(int, sys.stdin.readline().split())))
b_list = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)
sums = 0

for i in range(s):
    sums += a_list[i] * b_list[i]
print(sums)
