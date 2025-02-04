import sys
from heapq import heappush, heappop


n = int(sys.stdin.readline())
heap = []

for _ in range(n):
    i = int(sys.stdin.readline())
    if i != 0:
        heappush(heap, (abs(i), i))
    else:
        if not heap:
            print(0)
        else:
            print(heappop(heap)[1])
