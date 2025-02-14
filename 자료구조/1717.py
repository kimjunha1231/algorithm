import sys

sys.setrecursionlimit(1000000)

input = sys.stdin.readline
N, M = map(int, input().split())
parent = [i for i in range(N + 1)]


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    rootx = find(x)
    rooty = find(y)
    if rootx != rooty:
        if rootx < rooty:
            parent[rooty] = rootx
        else:
            parent[rootx] = rooty


for _ in range(M):
    num_list = list(map(int, input().split()))
    if num_list[1] > N or num_list[2] > N:
        continue
    if num_list[0] == 0:
        union(num_list[1], num_list[2])
    else:
        if find(num_list[1]) == find(num_list[2]):
            print("YES")
        else:
            print("NO")
