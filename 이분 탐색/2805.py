import sys

N, M = map(int, sys.stdin.readline().split())

N_list = list(map(int, sys.stdin.readline().split()))


def binary():
    left = 0
    right = max(N_list)
    result = 0

    while left <= right:
        total = 0
        mid = (right + left) // 2
        for n in N_list:
            if n > mid:
                total += n - mid
        if total >= M:
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    print(result)


binary()
