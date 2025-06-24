import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

first, second = map(int, input().split())

m = int(input())
graph = [[] for _ in range(N + 1)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
count = [-1] * (N + 1)
q = deque([first])
visited = [False] * (N + 1)
count[first] = 0
visited[first] = True
while q:
    a = q.popleft()
    for v in graph[a]:
        if not visited[v]:
            visited[v] = True
            q.append(v)
            count[v] = count[a] + 1


print(count[second])
