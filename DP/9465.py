import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):

    n = int(input())
    n_list = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0] * n for _ in range(2)]
    if n == 1:
        print(max(n_list[0][0], n_list[1][0]))
        continue

    dp[0][0] = n_list[0][0]
    dp[1][0] = n_list[1][0]
    dp[0][1] = n_list[0][1] + dp[1][0]
    dp[1][1] = n_list[1][1] + dp[0][0]

    for i in range(2, n):
        dp[1][i] = max(dp[0][i - 1], dp[0][i - 2]) + n_list[1][i]
        dp[0][i] = max(dp[1][i - 1], dp[1][i - 2]) + n_list[0][i]

    print(max(dp[0][n - 1], dp[1][n - 1]))
