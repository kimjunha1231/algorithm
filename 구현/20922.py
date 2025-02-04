import sys
from collections import defaultdict

N, K = map(int, sys.stdin.readline().split())


count = 0
a = list(map(int, sys.stdin.readline().split()))
dicts = defaultdict(int)
left = 0

for i in range(N):

    dicts[a[i]] += 1

    while dicts[a[i]] > K:
        dicts[a[left]] -= 1
        left += 1
    count = max(count, i - left + 1)

print(count)
