import sys
from collections import deque, defaultdict

N = int(sys.stdin.readline())

n_list = []
for i in range(N):
    n_list.append(list(map(int, sys.stdin.readline().strip())))
direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def bfs(graph, start, end):
    queue = deque([[start, end]])
    graph[start][end] = 0
    count = 1
    while queue:
        nx, ny = queue.popleft()
        for dx, dy in direction:
            x, y = nx + dx, ny + dy
            if 0 <= x < N and 0 <= y < N and n_list[x][y] == 1:
                graph[x][y] = 0
                count += 1
                queue.append([x, y])
    return count


result = []
for i in range(N):
    for l in range(N):
        if n_list[i][l] == 1:
            result.append(bfs(n_list, i, l))
print(len(result))
print("\n".join(map(str, sorted(result))))
