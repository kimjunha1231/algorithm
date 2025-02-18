import sys

n, k = map(int, sys.stdin.readline().split())

n_list = []
for i in range(1, n + 1):
    if n % i == 0:
        n_list.append(i)

if len(n_list) >= k:
    print(n_list[k - 1])
else:
    print(0)
