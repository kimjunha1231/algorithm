import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

def bfs (graph, start, N ):
    dist= [-1] *(N+1)
    dist[start]= 0
    di = deque([start])
    result = 0
    
    while di:
        cur= di.popleft()
        for c in graph[cur]:
                if dist[c] == -1 :
                    di.append(c)
                    dist[c] = dist[cur] +1 
                    result+= dist[c]
    return result
                    
min_sum = float('inf')
relation_list = [[] for _ in range(N+1)] 
for _ in range(M):
    a,b = map(int, input().split())
    relation_list[a].append(b)
    relation_list[b].append(a)
result = 0
for i in range(1, N+1):
    re= bfs(relation_list, i, N)
    if re < min_sum:
        min_sum= re
        result= i

print(result)
    