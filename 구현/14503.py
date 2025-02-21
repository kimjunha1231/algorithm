import sys

n, m = map(int, sys.stdin.readline().split())

x, y, di = map(int, sys.stdin.readline().split())

graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))
count = 0
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

while True:
    o_in = False
    if graph[x][y] == 0:
        graph[x][y] = 2
        count += 1

    for _ in range(4):
        di = (di + 3) % 4
        nowx, nowy = x + direction[di][0], y + direction[di][1]
        if n > nowx >= 0 and m > nowy >= 0 and graph[nowx][nowy] == 0:
            x, y = nowx, nowy
            o_in = True
            break
    if not o_in:
        if di <= 1:
            nowx, nowy = direction[di + 2]
        else:
            nowx, nowy = direction[di - 2]

        nowx, nowy = x + nowx, y + nowy
        if n > nowx >= 0 and m > nowy >= 0 and graph[nowx][nowy] != 1:
            x, y = nowx, nowy
        else:
            print(count)
            sys.exit()
