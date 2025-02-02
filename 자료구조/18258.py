import sys
from collections import deque

N = int(sys.stdin.readline())

q_list = deque()
result = []
for i in range(N):
    n_list = sys.stdin.readline().split()

    if n_list[0] == "push":
        q_list.append(n_list[1])
    elif n_list[0] == "pop":
        if q_list:
            result.append(q_list.popleft())
        else:
            result.append(-1)
    elif n_list[0] == "size":
        result.append(len(q_list))
    elif n_list[0] == "empty":
        if q_list:
            result.append(0)
        else:
            result.append(1)
    elif n_list[0] == "front":
        if q_list:
            result.append(q_list[0])
        else:
            result.append(-1)
    else:
        if q_list:
            result.append(q_list[-1])
        else:
            result.append(-1)

for _ in result:
    print(_)
