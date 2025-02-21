import sys
from itertools import combinations

N = int(sys.stdin.readline())
person = [i for i in range(0, N)]
n_list = []

for i in range(N):
    n_list.append(list(map(int, sys.stdin.readline().split())))
com = list(combinations(person, N // 2))

mins = float("inf")
for c in com:
    link_team = list(set(person) - set(c))
    start_team = list(c)
    link_socre = 0
    start_socre = 0
    for s1, s2 in combinations(start_team, 2):
        start_socre += n_list[s1][s2] + n_list[s2][s1]
    for l1, l2 in combinations(link_team, 2):
        link_socre += n_list[l1][l2] + n_list[l2][l1]
    mins = min(mins, abs(start_socre - link_socre))
    if mins == 0:
        break
print(mins)
