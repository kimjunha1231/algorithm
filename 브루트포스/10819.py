import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())

n_list = list(map(int, input().split()))
per_n_list = permutations(n_list)
maxs = 0
for per in per_n_list:
    result = 0
    for i in range(N - 1):
        result += abs(per[i] - per[i + 1])
    maxs = max(maxs, result)


print(maxs)
