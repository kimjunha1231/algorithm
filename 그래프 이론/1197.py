import sys
from operator import itemgetter

V, E = map(int, sys.stdin.readline().split())

edges = []
for i in range(E):
    A, B, C = map(int, sys.stdin.readline().split())
    edges.append((A, B, C))
edges = sorted(edges, key=itemgetter(2))
