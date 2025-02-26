import sys
from collections import deque, defaultdict

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

dic = defaultdict(list)
for i in range(M):
    n1, n2 = map(int, sys.stdin.readline().split())
    dic[n1].append(n2)
    dic[n2].append(n1)


def bfs(graph, start):
    queue = deque([start])
    visited = []
    visited.append(start)
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if i not in visited:

                queue.append(i)
                visited.append(i)
    return len(visited) - 1


print(bfs(dic, 1))
