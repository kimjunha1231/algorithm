import sys

input = sys.stdin.readline


N = int(input())


a_list = list(map(int, input().split()))
dp = [1] * N

for i in range(N):
    for j in range(i):
        if a_list[i] < a_list[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))
