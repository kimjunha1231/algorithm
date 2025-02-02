import sys

N = int(sys.stdin.readline())
container = []


for i in range(N):
    container.append(list(map(int, sys.stdin.readline().split())))

container.sort(key=lambda x: x[0])
idx = 0
max_height = max(container, key=lambda x: x[1])[1]
for q in range(N):
    if max_height == container[q][1]:
        idx = q


result = 0
height = container[0]


if N == 1:
    print(container[0][1])
else:
    for j in range(1, idx):
        if height[1] < container[j][1]:
            result += (container[j][0] - height[0]) * height[1]
            height = container[j]

    result += (container[idx][0] - height[0]) * height[1]

    end_idx = idx
    for n in range(idx, N):
        if max_height == container[n][1]:
            end_idx = n
    result += (container[end_idx][0] - container[idx][0] + 1) * max_height
    height = container[-1]
    for k in range(N - 1, end_idx, -1):
        if height[1] < container[k][1]:
            result += (height[0] - container[k][0]) * height[1]
            height = container[k]
    result += abs(container[end_idx][0] - height[0]) * height[1]
    print(result)
