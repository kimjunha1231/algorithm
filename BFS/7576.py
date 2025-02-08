import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())


graph = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]


index_que = deque()

for i in range(M):
    for j in range(N):
        if graph[i][j] == 1:
            index_que.append((i, j))


derection = [(0, 1), (0, -1), (1, 0), (-1, 0)]
count = 0

while index_que:
    for _ in range(len(index_que)):
        nx, ny = index_que.popleft()
        for dix, diy in derection:
            dx, dy = nx + dix, ny + diy
            if M > dx >= 0 and N > dy >= 0 and graph[dx][dy] == 0:
                graph[dx][dy] = 1
                index_que.append((dx, dy))

    count += 1


for j in graph:
    if 0 in j:
        print(-1)
        exit()
print(count - 1)
