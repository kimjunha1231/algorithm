import sys
from itertools import permutations

N = int(sys.stdin.readline())
n_list = [i for i in range(1, N + 1)]
result = list(permutations(n_list))
for re in result:
    print(" ".join(map(str, re)))
