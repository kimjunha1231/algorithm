import sys
from collections import deque

input = sys.stdin.readline


lists = [[0] * 19 for _ in range(19)]

for i in range(19):
    lists[i] = list(map(int, input().split()))


def find(start, x, y):

    direction = [(1, 0), (0, 1), (-1, 1), (1, 1)]

    for dx, dy in direction:
        count = 1
        nx, ny = x + dx, y + dy
        while 0 <= nx < 19 and 0 <= ny < 19 and lists[nx][ny] == start:
            count += 1
            if count == 5:
                prev_x, prev_y = x - dx, y - dy
                next_x, next_y = nx + dx, ny + dy

                if (
                    0 <= prev_x < 19
                    and 0 <= prev_y < 19
                    and lists[prev_x][prev_y] == start
                ):
                    break

                if (
                    0 <= next_x < 19
                    and 0 <= next_y < 19
                    and lists[next_x][next_y] == start
                ):
                    break

                print(start)
                print(x + 1, y + 1)
                sys.exit(0)
            nx, ny = nx + dx, ny + dy
    return count


for i in range(19):
    for j in range(19):
        if lists[i][j] != 0:  # 돌이 있는 경우만 검사
            find(lists[i][j], i, j)

print(0)
