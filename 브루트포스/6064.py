import sys
from math import gcd


input = sys.stdin.readline

T = int(input())

for _ in range(T):
    M, N, x, y = map(int, input().split())
    x1 = 1
    y1 = 1
    count = -1
    max_time = M * N // gcd(M, N)
    k = x
    while k <= max_time:
        if (k - 1) % N + 1 == y:
            count = k
            break
        k += M
    print(count)
