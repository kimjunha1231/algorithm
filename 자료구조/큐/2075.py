import sys
import heapq

N = int(sys.stdin.readline())
n_list = []

for i in range(N):
    ans = list(map(int, sys.stdin.readline().split()))
    for a in ans:
        heapq.heappush(n_list, a)
        if len(n_list) > N:
            heapq.heappop(n_list)
print(n_list[0])
