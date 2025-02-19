import sys

N = int(sys.stdin.readline())
n_list = []
for i in range(N):
    t, p = map(int, sys.stdin.readline().split())
    n_list.append((t, p))
output = []


dp = [0] * (N + 1)

for i in range(N - 1, -1, -1):  # 거꾸로 진행
    time, pay = n_list[i]
    if i + time <= N:  # 상담을 완료할 수 있는 경우
        dp[i] = max(dp[i + 1], pay + dp[i + time])
    else:
        dp[i] = dp[i + 1]

print(dp[0])
