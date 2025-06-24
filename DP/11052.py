import sys

input = sys.stdin.readline

N = int(input())
n_list = list(map(int, input().split()))
dp = [0] * (N + 1)

for i in range(1, N + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i], dp[i - j] + n_list[j - 1])

print(max(dp))
