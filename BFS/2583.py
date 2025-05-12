import sys
from collections import deque

input = sys.stdin.readline


M, N, K = map(int, input().split())
visited = [[False] * N for i in range(M)]


for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            visited[y][x] = True

direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
result_list = []


def bfs(y, x):
    visited[y][x] = True
    count = 1
    dq = deque()
    dq.appendleft((y, x))
    while dq:
        y, x = dq.popleft()
        for dx, dy in direction:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[ny][nx]:
                count += 1
                dq.append((ny, nx))
                visited[ny][nx] = True
    result_list.append(count)


for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)

result_list.sort()

print(len(result_list))
print(" ".join(map(str, result_list)))
