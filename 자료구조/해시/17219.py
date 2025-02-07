import sys

N, M = map(int, sys.stdin.readline().split())
dicts = {}

add_list = []
for _ in range(N):
    add, password = sys.stdin.readline().rstrip().split()
    dicts[add] = password
for i in range(M):
    index = sys.stdin.readline().strip()
    print(dicts[index])
