import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

n_list = deque([i for i in range(1, N + 1)])
result = []
while n_list:
    for _ in range(K - 1):
        n_list.append(n_list.popleft())
    result.append(n_list.popleft())
print("<", end="")
print(", ".join(map(str, result)), end="")
print(">")
