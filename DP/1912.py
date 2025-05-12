import sys


input = sys.stdin.readline

n = int(input())

n_list = list(map(int, input().split()))


result = n_list[0]
current_sum = n_list[0]

for i in range(1, n):
    current_sum = max(n_list[i], current_sum + n_list[i])
    result = max(current_sum, result)

print(result)
