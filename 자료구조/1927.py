import heapq
import sys


N = int(sys.stdin.readline())
n_list = []

for i in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(n_list) > 0:
            print(heapq.heappop(n_list))
        else:
            print(0)
    else:
        heapq.heappush(n_list, x)
