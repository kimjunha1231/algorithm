import sys

input = sys.stdin.readline

N = int(input())
n_list = []
for i in range(N):
    n_list.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        for k in range(N):
            if n_list[j][i] and n_list[i][k]:
                n_list[j][k] = 1
for row in n_list:
    print(" ".join(map(str, row)))
