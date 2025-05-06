import sys
from collections import deque

input = sys.stdin.readline


N = int(input())


n_list = list(list(map(int, input().split())) for _ in range(N))


direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]

max_height = max(map(max, n_list))


def bfs(x, y, height):
    dq = deque()
    dq.append((x, y))
    visited[x][y] = True
    while dq:
        x, y = dq.popleft()
        for dx, dy in direction:
            nx = x + dx
            ny = y + dy
            if (
                0 <= nx < N
                and 0 <= ny < N
                and not visited[nx][ny]
                and n_list[nx][ny] > height
            ):
                visited[nx][ny] = True
                dq.append((nx, ny))


result = 0
for h in range(0, max_height + 1):
    visited = [[False] * N for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if n_list[i][j] > h and not visited[i][j]:
                bfs(i, j, h)
                count += 1
    result = max(count, result)
print(result)
