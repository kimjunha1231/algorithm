import sys
from itertools import combinations


N, M = map(int, sys.stdin.readline().split())

n_list = list(i for i in range(1, N + 1))

result = combinations(n_list, M)
for i in result:
    print(" ".join(map(str, i)))
