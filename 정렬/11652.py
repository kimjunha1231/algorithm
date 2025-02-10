import sys

N = int(sys.stdin.readline())
lists = {}

for i in range(N):
    num = int(sys.stdin.readline())
    if num in lists:
        lists[num] += 1
    else:
        lists[num] = 1
max_index = max(lists.values())
max_value = []
for v, k in lists.items():
    if k == max_index:
        max_value.append(v)

print(min(max_value))
