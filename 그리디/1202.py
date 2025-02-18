import sys
import heapq
from operator import itemgetter


n, k = map(int, sys.stdin.readline().split())
vo = []
k_list = []
for i in range(n):
    vo.append(list(map(int, sys.stdin.readline().split())))

for i in range(k):
    k_list.append(int(sys.stdin.readline()))

vo.sort()
k_list.sort()
result = 0
max_heap = []
index = 0
for i in range(k):

    while index < n and vo[index][0] <= k_list[i]:
        heapq.heappush(max_heap, -vo[index][1])
        index += 1
    if max_heap:
        result += -heapq.heappop(max_heap)


print(result)
