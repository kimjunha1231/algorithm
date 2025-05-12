import sys
from collections import deque

input = sys.stdin.readline

direction = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]


def bfs(y, x):
    dq = deque()
    dq.append((y, x))
    visited[y][x] = True
    while dq:
        y, x = dq.popleft()
        for dy, dx in direction:
            ny = dy + y
            nx = dx + x
            if (
                0 <= nx < w
                and 0 <= ny < h
                and not visited[ny][nx]
                and line[ny][nx] == 1
            ):
                visited[ny][nx] = True
                dq.append((ny, nx))


while True:

    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    visited = [[False] * w for _ in range(h)]
    count = 0

    line = [list(map(int, input().split())) for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and line[i][j] == 1:
                bfs(i, j)
                count += 1

    print(count)
