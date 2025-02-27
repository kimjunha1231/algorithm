import sys
from collections import deque


N, K = map(int, sys.stdin.readline().split())


def bfs(start, end):
    count = 0
    queue = deque([[start, count]])
    visited = set()
    visited.add(start)
    while queue:
        q, time = queue.popleft()
        if q == end:
            print(time)
            break
        q1, q2, q3 = q + 1, q * 2, q - 1
        if q1 not in visited and 100000 >= q1 >= 0:
            queue.append([q1, time + 1])
            visited.add(q1)
        if q2 not in visited and 100000 >= q2 >= 0:
            queue.append([q2, time + 1])
            visited.add(q2)
        if q3 not in visited and 100000 >= q3 >= 0:
            queue.append([q3, time + 1])
            visited.add(q3)


bfs(N, K)
