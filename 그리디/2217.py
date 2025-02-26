import sys
from itertools import combinations

N = int(sys.stdin.readline())

n_list = []
for i in range(N):
    n_list.append(int(sys.stdin.readline()))

n_list.sort()
maxs = n_list[-1]

for i in range(0, N):

    maxs = max(n_list[i] * (N - i), maxs)
print(maxs)
