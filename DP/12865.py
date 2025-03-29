import sys

N, K = map(int, sys.stdin.readline().split())

n_list = []
for i in range(N):
    w, v = map(int, sys.stdin.readline().split())
    n_list.append((w, v))

result = 0
dp = [0] * (K + 1)

for weight, value in n_list:
    for w in range(K, weight - 1, -1):  # 뒤에서부터 업데이트!
        dp[w] = max(dp[w], dp[w - weight] + value)


print(max(dp))
