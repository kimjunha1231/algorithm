import sys
from collections import defaultdict

input = sys.stdin.readline
N, M = map(int, input().rstrip().split())


dicts = defaultdict(list)
member_dicts = {}
for _ in range(N):

    group = input().strip()
    count = int(input())

    for _ in range(count):
        member = input().strip()
        dicts[group].append(member)
        member_dicts[member] = group
for _ in range(M):
    que = input().strip()
    qes = int(input())
    if qes == 1:
        print(member_dicts[que])
    else:
        print("\n".join(sorted(dicts[que])))
