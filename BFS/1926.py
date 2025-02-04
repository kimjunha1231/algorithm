import sys
from collections import deque


n, m = map(int, sys.stdin.readline().split())

paint = []

for i in range(n):
    paint.append(list(map(int, sys.stdin.readline().strip().split())))


def bfs(paint, start, visited):

    queue = deque([(start, visited)])
    paint[start][visited] = 0

    count = 1
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while queue:
        curx, cury = queue.popleft()
        for dx, dy in directions:
            nowx, nowy = dx + curx, dy + cury
            if (
                nowx >= 0
                and nowx < n
                and nowy < m
                and nowy >= 0
                and paint[nowx][nowy] == 1
            ):
                paint[nowx][nowy] = 0
                queue.append([nowx, nowy])
                count += 1
    return count


result = []
for x in range(n):
    for y in range(m):
        if paint[x][y] == 1:
            result.append(bfs(paint, x, y))

if len(result) != 0:

    sys.stdout.write(str(len(result)) + "\n")
    result.sort()
    sys.stdout.write(str(result[-1]))
else:
    sys.stdout.write("0\n")
    sys.stdout.write("0")
