import sys

input = sys.stdin.readline


N, K = map(int, input().split())
n_list = list(map(int, input().split()))


result = float("inf")

count = 0
left = 0
for right in range(N):
    if n_list[right] == 1:
        count += 1
    while count == K:
        result = min(result, right - left + 1)
        if n_list[left] == 1:
            count -= 1
        left += 1


if result == float("inf"):
    print(-1)
else:
    print(result)
