import sys

input = sys.stdin.readline

N = int(input())

n_list = list(list(map(int, input().split())) for _ in range(N))

dp = [[0] * 3 for _ in range(N)]
dp[0] = n_list[0]

for i in range(1, N):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + n_list[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + n_list[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + n_list[i][2]

print(min(dp[-1]))
