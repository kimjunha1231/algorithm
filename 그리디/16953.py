import sys
from collections import deque

A, B = map(int, sys.stdin.readline().split())
count = 0


def bfs(a, b):
    queue = deque([(A, 1)])
    while queue:
        num, count = queue.popleft()
        if num == B:
            return count
        if num * 2 <= B:
            queue.append((num * 2, count + 1))
        if num * 10 + 1 <= B:
            queue.append((num * 10 + 1, count + 1))
    return -1


print(bfs(A, B))
