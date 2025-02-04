import sys
from collections import deque

# 입력 받기
N, M = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

# 이동 방향 (상, 하, 좌, 우)
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]


# BFS 함수 정의
def bfs(start):
    queue = deque([start])  # BFS를 위한 큐
    while queue:
        curx, cury = queue.popleft()  # 현재 위치 꺼내기

        for dx, dy in directions:
            nx, ny = curx + dx, cury + dy

            # 범위 안에 있고, 이동 가능한 곳이면 탐색 진행
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                graph[nx][ny] = graph[curx][cury] + 1  # 거리 갱신
                queue.append((nx, ny))

    return graph[N - 1][M - 1]  # 도착점의 거리 값 반환


# 시작점이 벽(0)인 경우 도달 불가능
if graph[0][0] == 0:
    print(-1)
else:
    print(bfs((0, 0)))
