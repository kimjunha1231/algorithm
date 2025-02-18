import sys
from collections import deque

N = int(sys.stdin.readline())
n_list = []

for i in range(N):
    n1, n2 = sys.stdin.readline().strip().split(".")
    n_list.append(n2)
n_list.sort()

queue = deque(n_list)
count = 0
while queue:
    num = queue.popleft()
    if not queue:
        count += 1
        print(num, end=" ")
        print(count)
        break
    if num == queue[0]:
        count += 1
    elif num != queue[0]:
        count += 1
        print(num, end=" ")
        print(count)
        count = 0
