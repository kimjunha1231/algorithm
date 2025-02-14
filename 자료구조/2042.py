import sys

input = sys.stdin.readline
N, M, K = map(int, input().split())
n_list = []
sum_list = [0] * (N + 1)
for i in range(N):
    n_list.append(int(input()))
    sum_list[i + 1] = sum_list[i] + n_list[i]

for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        diff = c - n_list[b - 1]
        n_list[b - 1] = c
        for k in range(b, N + 1):
            sum_list[k] += diff
    elif a == 2:
        sys.stdout.write(str(sum_list[c] - sum_list[b - 1]) + "\n")
