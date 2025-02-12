import sys

N, C = map(int, sys.stdin.readline().split())

dicts = {}
lists = []

for i in sys.stdin.readline().split():
    if i in dicts:
        dicts[i] += 1
    else:
        dicts[i] = 1

sorted_items = sorted(dicts.items(), key=lambda x: -x[1])

for num, count in sorted_items:
    print(f"{num} " * count, end="")
