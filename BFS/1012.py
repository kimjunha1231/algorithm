import sys
from collections import deque

T = int(sys.stdin.readline())

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(graph, y, x):
    queue = deque([[y, x]])
    graph[y][x] = 0
    count = 1
    while queue:
        ny, nx = queue.popleft()
        for dy, dx in direction:
            x, y = dx + nx, dy + ny
            if 0 <= x < M and 0 <= y < N and graph[y][x] == 1:
                count += 1
                graph[y][x] = 0
                queue.append([y, x])


for _ in range(T):
    count = 0
    M, N, K = map(int, sys.stdin.readline().split())
    n_list = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        n_list[y][x] = 1
    for i in range(N):
        for j in range(M):
            if n_list[i][j] == 1:
                bfs(n_list, i, j)
                count += 1
    print(count)
