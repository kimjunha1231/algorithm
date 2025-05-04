import sys
import copy
from collections import deque
from itertools import combinations

input = sys.stdin.readline


N, M = map(int, input().split())
virus_lab = [list(map(int, input().split())) for _ in range(N)]


empty = []

direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for i in range(N):
    for j in range(M):
        if virus_lab[i][j] == 0:
            empty.append((i, j))


def spread(temp_lab):
    dq = deque()
    for i in range(N):
        for j in range(M):
            if temp_lab[i][j] == 2:
                dq.append((i, j))
    while dq:
        x, y = dq.popleft()
        for dx, dy in direction:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if temp_lab[nx][ny] == 0:
                    temp_lab[nx][ny] = 2
                    dq.append((nx, ny))


max_safe = 0


def get_safe_area(temp_lab):
    return sum(row.count(0) for row in temp_lab)


for walls in combinations(empty, 3):
    temp_lab = copy.deepcopy(virus_lab)
    for x, y in walls:
        temp_lab[x][y] = 1
    spread(temp_lab)
    max_safe = max(max_safe, get_safe_area(temp_lab))
print(max_safe)
