import sys

N = int(sys.stdin.readline())

n_list = [0] * (N + 1)
for i in range(1, N + 1):
    n_list[i] = int(sys.stdin.readline())

dp = [0] * (N + 1)


if N >= 1:
    dp[1] = n_list[1]
if N >= 2:
    dp[2] = n_list[1] + n_list[2]
if N >= 3:
    for i in range(3, N + 1):
        dp[i] = max(dp[i - 2] + n_list[i], dp[i - 3] + n_list[i - 1] + n_list[i])

print(dp[N])
