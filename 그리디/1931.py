import sys
from operator import itemgetter

N = int(sys.stdin.readline())
n_list = []
for _ in range(N):
    n1, n2 = map(int, sys.stdin.readline().split())
    n_list.append((n1, n2))
result = [(0, 0)]
sorted_n_list = sorted(n_list, key=itemgetter(1, 0))


for s1, s2 in sorted_n_list:
    if s1 >= result[-1][1]:
        result.append((s1, s2))

print(len(result) - 1)
