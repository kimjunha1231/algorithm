import sys

N = int(sys.stdin.readline())

n_list = list(map(int, sys.stdin.readline().split()))
n_list.sort()
results = 0
for i in range(N):
    results += n_list[i] * (N - i)
print(results)
