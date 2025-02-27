import sys
from collections import deque, defaultdict


N = int(sys.stdin.readline())

dic = defaultdict(list)

for _ in range(N - 1):
    n1, n2 = map(int, sys.stdin.readline().split())
    dic[n1].append(n2)
    dic[n2].append(n1)

parent_list = defaultdict(list)


def bfs(graph, start):
    queue = deque([start])
    visited = set([start])
    while queue:
        p = queue.popleft()
        for i in graph[p]:
            if i not in visited:
                queue.append(i)
                visited.add(i)
                parent_list[i] = p


bfs(dic, 1)
for i in range(2, N + 1):
    print(parent_list[i])
