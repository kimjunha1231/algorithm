import sys

input = sys.stdin.readline
n_list = []
result_list = []

count = 0
position = {}
for _ in range(5):
    n_list.append(list(map(int, input().split())))
for _ in range(5):
    result_list.append(list(map(int, input().split())))
for i in range(5):
    for j in range(5):
        position[n_list[i][j]] = (i, j)


def bing_count():
    bing = 0
    for row in n_list:
        if all(num == 0 for num in row):
            bing += 1
    for col in range(5):
        if all(n_list[row][col] == 0 for row in range(5)):
            bing += 1

    if all(n_list[i][i] == 0 for i in range(5)):
        bing += 1
    if all(n_list[i][4 - i] == 0 for i in range(5)):
        bing += 1
    return bing


for i in range(5):
    for j in range(5):
        num = result_list[i][j]
        count += 1
        if num in position:
            x, y = position[num]
            n_list[x][y] = 0

        if bing_count() >= 3:
            print(count)
            exit()
