import sys

N, S = map(int, sys.stdin.readline().split())

list = list(map(int, sys.stdin.readline().split()))
count = 0


def backtrack(idx, visited):
    global count
    if idx >= N:
        return
    visited += list[idx]
    if visited == S:
        count += 1
    backtrack(idx + 1, visited)

    backtrack(idx + 1, visited - list[idx])


backtrack(0, 0)

print(count)
