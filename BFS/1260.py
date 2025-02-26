import sys

from collections import defaultdict, deque

N, M, V = map(int, sys.stdin.readline().split())
dic = defaultdict(list)

for i in range(M):
    n1, n2 = map(int, sys.stdin.readline().split())
    dic[n1].append(n2)
    dic[n2].append(n1)


def bfs(graph, start):
    queue = deque([start])
    visited = {start}
    while queue:
        n = queue.popleft()
        print(n, end=" ")
        for i in sorted(graph[n]):

            if i not in visited:
                visited.add(i)
                queue.append(i)


def dfs(graph, start, visited):
    visited.append(start)
    print(start, end=" ")
    for i in sorted(graph[start]):
        if i not in visited:
            dfs(graph, i, visited)


dfs(dic, V, [])

print()
bfs(dic, V)
