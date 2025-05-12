import sys

input = sys.stdin.readline

n = int(input())

n_list = list(list(map(int, input().split())) for _ in range(n))
dp = [[0] * len(k) for k in n_list]
dp[0] = n_list[0]
for i in range(1, n):
    for j in range(len(n_list[i])):
        if j == 0:
            dp[i][j] = dp[i - 1][j] + n_list[i][j]
        elif j == i:
            dp[i][j] = dp[i - 1][j - 1] + n_list[i][j]
        else:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + n_list[i][j]
print(max(dp[-1]))
