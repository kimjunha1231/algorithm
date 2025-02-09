import sys


def backtrack(depth, sequence, visited, N, M):

    if depth == M:
        print(" ".join(map(str, sequence)))
        return

    for num in range(1, N + 1):
        if not visited[num]:
            visited[num] = True
            sequence.append(num)
            backtrack(depth + 1, sequence, visited, N, M)
            sequence.pop()
            visited[num] = False


N, M = map(int, sys.stdin.readline().split())

visited = [False for _ in range(N + 1)]
result = []

backtrack(0, result, visited, N, M)
