import sys

input = sys.stdin.readline

N = int(input())
n_list = list(map(int, input().split()))

dp = [0] * N
for i in range(N):
    dp[i] = n_list[i]
    for j in range(i):
        if n_list[j] < n_list[i]:
            dp[i] = max(dp[i], dp[j] + n_list[i])

print(max(dp))
