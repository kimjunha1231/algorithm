import sys

N, M = map(int, sys.stdin.readline().split())

N_list = [0]
N_list = list(map(int, sys.stdin.readline().split()))


for i in range(1, N):
    N_list[i] += N_list[i - 1]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    if i - 2 >= 0:
        print(N_list[j - 1] - N_list[i - 2])
    else:
        print(N_list[j - 1])
