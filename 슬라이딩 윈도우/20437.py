import sys


input = sys.stdin.readline

T = int(input())

for i in range(T):
    dict = {}
    w = input().strip()
    k = int(input())
    result1 = float("inf")
    result2 = 0
    for i, v in enumerate(w):
        if v not in dict:
            dict[v] = [i]
        else:
            dict[v].append(i)
    for i, v in dict.items():
        if len(v) >= k:
            for i in range(len(v) - k + 1):
                result1 = min(result1, v[i + k - 1] - v[i] + 1)
                result2 = max(result2, v[i + k - 1] - v[i] + 1)

    if result1 == "inf" or result2 == 0:
        print(-1)
    else:
        print(result1, result2)
