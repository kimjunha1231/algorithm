import sys


input = sys.stdin.readline

n = int(input())
n_list = list(int(input()) for i in range(n))
dp = [0] * n
dp[0] = n_list[0]
if n > 1:
    dp[1] = n_list[1] + dp[0]
for i in range(2, n):
    dp[i] = max(dp[i - 1], dp[i - 2] + n_list[i], n_list[i] + n_list[i - 1])
    if i > 2:
        dp[i] = max(
            dp[i - 1], dp[i - 2] + n_list[i], n_list[i] + n_list[i - 1] + dp[i - 3]
        )
print(max(dp))
