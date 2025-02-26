import sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
length = 1
n_list = [[0] * N for _ in range(N)]
n_list[0][0] = 1
direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]
for _ in range(K):
    x, y = map(int, sys.stdin.readline().split())
    n_list[x - 1][y - 1] = 2
L = int(sys.stdin.readline())
count = 0
sec_list = []
for _ in range(L):
    second, di = sys.stdin.readline().split()
    sec_list.append((second, di))

dire = 3
x, y = 0, 0

visited = [(0, 0)]
while True:
    count += 1
    dx, dy = direction[dire]
    nowx, nowy = dx + x, dy + y

    if 0 <= nowx < N and 0 <= nowy < N and n_list[nowx][nowy] != 1:

        visited.append((nowx, nowy))
        if n_list[nowx][nowy] == 0:
            startx, starty = visited.pop(0)
            n_list[startx][starty] = 0
        x, y = nowx, nowy
        n_list[nowx][nowy] = 1
    else:

        print(count)
        break

    if sec_list:
        if count == int(sec_list[0][0]):
            sec, d = sec_list.pop(0)

            if d == "D":
                dire = (dire + 4 - 1) % 4
            else:
                dire = (dire + 4 + 1) % 4
