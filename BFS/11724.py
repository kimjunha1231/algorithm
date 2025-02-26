import sys
from collections import defaultdict, deque

N, M = map(int, sys.stdin.readline().split())

dic = defaultdict(list)

visited = set()


def bfs(graph, start):
    queue = deque([start])
    visited.add(start)
    while queue:
        node = queue.popleft()
        for i in dic[node]:
            if i not in visited:
                queue.append(i)
                visited.add(i)


count = 0
for i in range(M):
    n1, n2 = map(int, sys.stdin.readline().split())
    dic[n1].append(n2)
    dic[n2].append(n1)
for key in dic.keys():
    if key not in visited:
        bfs(dic, key)
        count += 1

print(count - len(dic) + N)
