import sys
from collections import deque
from operator import itemgetter

N, M, K = map(int, sys.stdin.readline().split())
s_list = {}
min = 0
max = 0
count = 0

for i in range(N):
    s, p = sys.stdin.readline().split()
    s_list[s] = int(p)


for i in range(K):
    ans = sys.stdin.readline().strip()
    min += s_list[ans]
    max += s_list[ans]
    del s_list[ans]
    count += 1
s_list = sorted(s_list.items(), key=itemgetter(1))
M = M - count

for i in range(M):
    min += s_list[i][1]
    max += s_list[-1 - i][1]

print(min, max)
