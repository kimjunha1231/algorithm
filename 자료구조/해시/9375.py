import sys
from collections import defaultdict

k = int(sys.stdin.readline())


for _ in range(k):
    n = int(sys.stdin.readline())

    mult = 1
    dicts = defaultdict(list)
    for i in range(n):
        a, b = sys.stdin.readline().rstrip().split()
        dicts[b].append(a)
    for key in dicts.keys():

        mult *= len(dicts[key]) + 1

    print(mult - 1)
