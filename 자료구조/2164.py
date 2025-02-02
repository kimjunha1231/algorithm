from collections import deque

N = int(input())
result = deque(range(1, N + 1))

while len(result) > 1:

    result.popleft()
    if len(result) == 1:
        break
    result.append(result.popleft())

print(result[0])
