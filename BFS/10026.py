import sys
from collections import deque
import copy

N = int(sys.stdin.readline())
n_list = []

direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def basicbfs(x, y, start):
    queue = deque([[x, y]])
    n_list[x][y] = 0
    while queue:
        nx, ny = queue.popleft()
        for dx, dy in direction:
            x, y = dx + nx, dy + ny
            if 0 <= x < N and 0 <= y < N and n_list[x][y] == start:
                n_list[x][y] = 0
                queue.append([x, y])


def bfs(x, y, start):
    queue = deque([[x, y]])
    n_list2[x][y] = 0
    while queue:
        nx, ny = queue.popleft()

        for dx, dy in direction:
            x, y = dx + nx, dy + ny
            if 0 <= x < N and 0 <= y < N and n_list2[x][y] == start:
                n_list2[x][y] = 0
                queue.append([x, y])


for i in range(N):
    n_list.append(list(sys.stdin.readline().strip()))


basic_count = 0
count = 0
n_list2 = copy.deepcopy(n_list)

for i in range(N):
    for j in range(N):
        if n_list[i][j] != 0:
            basicbfs(i, j, n_list[i][j])
            basic_count += 1
for i in range(N):
    for j in range(N):
        if n_list2[i][j] == "G":
            n_list2[i][j] = "R"
for i in range(N):
    for j in range(N):
        if n_list2[i][j] != 0:
            bfs(i, j, n_list2[i][j])
            count += 1
print(basic_count, end=" ")
print(count)
