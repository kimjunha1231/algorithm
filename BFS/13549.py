import sys
from collections import deque

input = sys.stdin.readline

Max = 100001
time = [0] * Max
visited = [False] * Max


dq = deque()
N, K = map(int, input().split())
dq.append(N)
visited[N] = True

while dq:
    now = dq.popleft()

    if now == K:
        print(time[now])
        break
    for time_now in [now * 2, now - 1, now + 1]:
        if 0 <= time_now < Max and not visited[time_now]:
            if time_now == now * 2:
                time[time_now] = time[now]
                visited[time_now] = True
                dq.appendleft(time_now)
            else:
                time[time_now] = time[now] + 1
                visited[time_now] = True
                dq.append(time_now)
