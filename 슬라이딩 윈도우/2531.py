import sys

input = sys.stdin.readline

N, d, k, c = map(int, input().split())
n_list = [int(input()) for _ in range(N)]

dict = {}
result = 0
for i in range(k):
    if n_list[i] not in dict:
        dict[n_list[i]] = 1
    else:
        dict[n_list[i]] += 1
if c not in dict:
    len_dict = len(dict) + 1
else:
    len_dict = len(dict)
result = max(result, len_dict)

for i in range(1, N):
    if n_list[(i + k - 1) % N] not in dict:
        dict[n_list[(i + k - 1) % N]] = 1
    else:
        dict[n_list[(i + k - 1) % N]] += 1
    dict[n_list[i - 1]] -= 1
    if dict[n_list[i - 1]] == 0:
        del dict[n_list[i - 1]]
    if c not in dict:
        len_dict = len(dict) + 1
    else:
        len_dict = len(dict)
    result = max(result, len_dict)
print(result)
