import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
n_list = deque(range(1, N + 1))

ans = list(map(int, sys.stdin.readline().split()))
count = 0


for i in ans:
    if i == n_list[0]:
        n_list.popleft()

    elif n_list.index(i) <= len(n_list) // 2:
        while True:
            if i == n_list[0]:
                n_list.popleft()
                break
            count += 1
            n_list.append(n_list.popleft())
    else:
        while True:
            if i == n_list[0]:
                n_list.popleft()
                break
            count += 1
            n_list.appendleft(n_list.pop())
print(count)
