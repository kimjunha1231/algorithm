import sys

N = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))

dp = [1] * N  # 자기 자신 하나는 포함하므로 모두 1로 초기화

for i in range(N):
    for j in range(i):
        if n_list[j] < n_list[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
