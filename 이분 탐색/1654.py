import sys

K, N = map(int, sys.stdin.readline().split())

k_list = []


def binary():
    left = 1
    right = max(k_list)

    result = 0
    while left <= right:
        count = 0
        mid = (left + right) // 2
        for k in k_list:
            count += k // mid
        if count >= N:
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    print(result)


for i in range(K):
    k_list.append(int(sys.stdin.readline()))

binary()
