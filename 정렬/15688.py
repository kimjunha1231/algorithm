import sys

N = int(sys.stdin.readline())

lists = [int(sys.stdin.readline()) for _ in range(N)]
print("\n".join(map(str, sorted(lists))))
