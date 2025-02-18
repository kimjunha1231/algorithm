import sys

N, K = map(int, sys.stdin.readline().split())
n_list = []
count = 0
for _ in range(N):
    n_list.append(int(sys.stdin.readline()))

for i in range(len(n_list) - 1, -1, -1):
    if K == 0:
        break
    if n_list[i] <= K:
        count += K // n_list[i]
        K %= n_list[i]


print(count)
